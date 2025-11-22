import streamlit as st
import copy
from collections import defaultdict

st.set_page_config(page_title="Asterisk Sudoku Solver", layout="centered")



def first(iterable, default=None):
    """Return the first element of an iterable, or default."""
    try:
        return next(iter(iterable))
    except StopIteration:
        return default

def different_values_constraint(A, a, B, b):
    """Constraint: Neighboring variables must have different values."""
    return a != b

class MinimalCSP:
    """Minimal CSP implementation for Sudoku."""
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.nassigns = 0

    def assign(self, var, val, assignment):
        """Assign value to variable."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Unassign variable."""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        """Count conflicts with assigned neighbors."""
        count = 0
        for var2 in self.neighbors.get(var, []):
            if var2 in assignment and not self.constraints(var, val, var2, assignment[var2]):
                count += 1
        return count
    
    def choices(self, var):
        """Return domain values."""
        return self.domains[var] 

# --- Sudoku Setup & Parsing ---

GRID_STR_RAW = (
    ".1.....6."
    "3.9.*.1.5"
    ".8*3.5*7."
    "..2.7.8.."
    ".*.6*8.*."
    "..8.9.2.."
    ".2*4.1*9."
    "9.4.*.6.1"
    ".3.....8."
)

def create_sudoku_csp(grid_str_raw):
    """Parses the grid and sets up the Asterisk Sudoku CSP."""
    
    asterisk_indices = []
    clean_grid = ""
    
    # 1. Parse Grid (Treat * as empty cells that need solving)
    for index, char in enumerate(grid_str_raw):
        if char == '*':
            asterisk_indices.append(index)
            clean_grid += '.'  
        else:
            clean_grid += char

    # 2. Define Variables and Domains
    variables = list(range(81))
    domains = {}
    
    for i in variables:
        char = clean_grid[i]
        if char.isdigit() and char != '0':
            domains[i] = [int(char)] # Fixed value
        else:
            domains[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Mutable

    # 3. Define Constraints (Neighbors)
    neighbors = {v: set() for v in variables}
    
    def add_clique(clique):
        for i in clique:
            for j in clique:
                if i != j:
                    neighbors[i].add(j)

    # Rows, Columns, Boxes
    for r in range(9): add_clique(list(range(r * 9, (r + 1) * 9)))
    for c in range(9): add_clique(list(range(c, 81, 9)))
    for row_start in [0, 3, 6]:
        for col_start in [0, 3, 6]:
            box = []
            for r in range(3):
                for c in range(3):
                    box.append((row_start + r) * 9 + (col_start + c))
            add_clique(box)
            
    # Asterisk Constraint (Crucial for Task 2)
    add_clique(asterisk_indices)
    
    # Convert sets to lists for stability
    for v in variables:
        neighbors[v] = sorted(list(neighbors[v]))

    return MinimalCSP(variables, domains, neighbors, different_values_constraint), asterisk_indices

# --- Heuristics ---

def mrv_variable(assignment, csp):
    """Minimum Remaining Values (MRV) Heuristic."""
    unassigned = [v for v in csp.variables if v not in assignment]
    if not unassigned:
        return None
        
    best_var = unassigned[0]
    min_legal_moves = 10 
    
    for var in unassigned:
        legal_moves = 0
        for val in csp.domains[var]:
            if csp.nconflicts(var, val, assignment) == 0:
                legal_moves += 1
        
        if legal_moves < min_legal_moves:
            min_legal_moves = legal_moves
            best_var = var
            if min_legal_moves <= 1:
                return best_var
                
    return best_var

def unordered_domain_values(var, assignment, csp):
    return csp.choices(var)

#backsearch

STEPS = [] 

def backtracking_search_with_steps(csp, select_unassigned_variable, order_domain_values):
    """
    Solves the CSP and records every assignment (forward) AND unassignment (backtrack).
    """
    STEPS.clear()
    
    # Initial state (Fixed values)
    initial_assignment = {
        var: csp.domains[var][0] for var, domain in csp.domains.items()
        if len(domain) == 1
    }
    STEPS.append(copy.deepcopy(initial_assignment))
    
    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment

        var = select_unassigned_variable(assignment, csp)
        
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                # 1. Assign Value
                csp.assign(var, value, assignment)
                
                # RECORD FORWARD STEP
                STEPS.append(copy.deepcopy(assignment))

                result = backtrack(assignment)
                if result is not None:
                    return result
                
                
                csp.unassign(var, assignment)
                
    
                STEPS.append(copy.deepcopy(assignment))
                
        return None

    final_assignment = backtrack(initial_assignment)
    return final_assignment


def calculate_stats(steps_history, current_index):
    #Calculate Forward + otal Operations
    forward_count = 0
    backward_count = 0
    
    for i in range(1, current_index + 1):
        prev_len = len(steps_history[i-1])
        curr_len = len(steps_history[i])
        
        if curr_len > prev_len:
            forward_count += 1
        elif curr_len < prev_len:
            backward_count += 1
            
    return forward_count, (forward_count + backward_count)

# --- Streamlit UI ---

@st.cache_data
def run_solver_and_setup_cache():
    """Run the solver once and cache the step history."""
    csp, asterisk_indices = create_sudoku_csp(GRID_STR_RAW)
    
    # Use MRV heuristic to ensure it runs fast
    backtracking_search_with_steps(
        csp, 
        select_unassigned_variable=mrv_variable,
        order_domain_values=unordered_domain_values
    )
    return STEPS, csp, asterisk_indices

def draw_board(assignment, asterisk_indices, initial_csp):
    #the Sudoku board highlighting
    st.markdown(
        """
        <style>
        .sudoku-container { display: flex; justify-content: center; margin-bottom: 15px; }
        .sudoku-grid { 
            display: grid; 
            grid-template-columns: repeat(9, 40px); 
            grid-template-rows: repeat(9, 40px); 
            border: 4px solid #333; 
        }
        .cell {
            width: 40px; height: 40px; 
            border: 1px solid #bbb;
            display: flex; justify-content: center; align-items: center;
            font-size: 18px; font-weight: bold; 
            color: #333; background-color: #fff;
        }
        /* Thicker borders for 3x3 boxes */
        .cell-thick-right { border-right: 3px solid #333 !important; }
        .cell-thick-bottom { border-bottom: 3px solid #333 !important; }
        
        /* Colors */
        .cell-prefilled { background-color: #e8f8f5; color: #0b5345; } 
        .cell-assigned { background-color: #d6eaf8; color: #154360; }
        .cell-asterisk { background-color: #fcf3cf !important; } /* Yellow */
        </style>
        """, unsafe_allow_html=True
    )

    board_html = '<div class="sudoku-container"><div class="sudoku-grid">'
    
    # Identify fixed  cells
    prefilled = {
        var: initial_csp.domains[var][0] 
        for var in initial_csp.variables if len(initial_csp.domains[var]) == 1
    }
    
    for i in range(81):
        r, c = divmod(i, 9)
        
        # Determine classes
        classes = ["cell"]
        if (c + 1) % 3 == 0 and c != 8: classes.append("cell-thick-right")
        if (r + 1) % 3 == 0 and r != 8: classes.append("cell-thick-bottom")
        
        # Highlight asterisk cells
        if i in asterisk_indices:
            classes.append("cell-asterisk")
        
        value = assignment.get(i, "")
        
        # Color logic
        if i in prefilled and value == prefilled[i]:
            classes.append("cell-prefilled")
        elif value:
            classes.append("cell-assigned")

        board_html += f'<div class="{" ".join(classes)}">{value}</div>'
    
    board_html += '</div></div>'
    st.markdown(board_html, unsafe_allow_html=True)

# --- Main Application ---

st.title(" Asterisk Sudoku Visualization")

# Initialize Data
if 'STEPS' not in st.session_state:
    with st.spinner("Solving Sudoku (using MRV heuristic)..."):
        steps_list, initial_csp, asterisk_indices = run_solver_and_setup_cache()
        st.session_state['STEPS'] = steps_list
        st.session_state['MAX_STEPS'] = len(steps_list) - 1
        st.session_state['INITIAL_CSP'] = initial_csp
        st.session_state['ASTERISK_INDICES'] = asterisk_indices
        st.session_state['step_index'] = 0

# Retrieve State
MAX_STEPS = st.session_state['MAX_STEPS']
current_step_index = st.session_state['step_index']
current_assignment = st.session_state['STEPS'][current_step_index]
asterisk_indices = st.session_state['ASTERISK_INDICES']
initial_csp = st.session_state['INITIAL_CSP']


fwd, total = calculate_stats(st.session_state['STEPS'], current_step_index)


st.subheader("Search Statistics")
col_a, col_c = st.columns(2)
col_a.metric("Assignments Made (Forward Steps)", fwd)
col_c.metric("Total Search Operations (Assignments + Backtracks)", total) # BWD counter removed

# Navigation Buttons
c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
with c1:
    if st.button(" **Start"):
        st.session_state['step_index'] = 0
        st.rerun()
with c2:
    if st.button("⬅️ Back"):
        if st.session_state['step_index'] > 0:
            st.session_state['step_index'] -= 1
            st.rerun()
with c3:
    if st.button("Next ➡️"):
        if st.session_state['step_index'] < MAX_STEPS:
            st.session_state['step_index'] += 1
            st.rerun()
with c4:
    if st.button("Finish !!"):
        st.session_state['step_index'] = MAX_STEPS
        st.rerun()

# draw board
st.write(f"**Current Step Index:** {current_step_index} / {MAX_STEPS}")
draw_board(current_assignment, asterisk_indices, initial_csp)

#sol msg
if current_step_index == MAX_STEPS:
    st.success("**Solution Complete!** The Asterisk constraint (aestrixked cells in yellow) is satisfied.")
