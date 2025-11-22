from src.CSPclass import CSP
from src.utils import *

def MapColoringCSP(colors, neighbors):
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSP(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)


from src.utils import different_values_constraint


def dinner_constraints(A, a, B, b):
    if a == b: return False
    conflict_pairs = [('A', 'B'), ('B', 'A'), 
                      ('B', 'E'), ('E', 'B'), 
                      ('B', 'C'), ('C', 'B')]
    
    if (A, B) in conflict_pairs:
        diff = abs(a - b)
        if diff == 1 or diff == 5:
            return False
    return True

def DinnerSeatingCSP():
    people = ['A', 'B', 'C', 'D', 'E']
    chairs = [1, 2, 3, 4, 5, 6]
    # Fully connected graph for AllDiff
    neighbors = {p: [o for o in people if o != p] for p in people}
    return CSP(people, UniversalDict(chairs), neighbors, dinner_constraints)


def SudokuCSP(grid, asterisk_indices=None):
   
    variables = list(range(81))
    domains = {}
    
    # 1. Define Domains
    for i in variables:
        char = grid[i]
        if char.isdigit() and char != '0':
            # Fixed value
            domains[i] = [int(char)]
        else:
            domains[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 2. Define Constraints (Neighbors)
    neighbors = {v: [] for v in variables}
    
    def add_clique(clique):
        for i in clique:
            for j in clique:
                if i != j and j not in neighbors[i]:
                    neighbors[i].append(j)

    # Rows
    for r in range(9):
        add_clique(list(range(r * 9, (r + 1) * 9)))
    # Columns
    for c in range(9):
        add_clique(list(range(c, 81, 9)))
    # Boxes
    for row_start in [0, 3, 6]:
        for col_start in [0, 3, 6]:
            box_indices = []
            for r in range(3):
                for c in range(3):
                    box_indices.append((row_start + r) * 9 + (col_start + c))
            add_clique(box_indices)

   #aestrik locations
    if asterisk_indices:
        add_clique(asterisk_indices)

    return CSP(variables, domains, neighbors, different_values_constraint)
