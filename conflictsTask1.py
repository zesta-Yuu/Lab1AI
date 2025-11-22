import copy
from pyvis.network import Network
from src.CSPS import DinnerSeatingCSP
from src.algorithms import AC3, backtracking_search

def visualize_constraints(csp):
    print(" making the constraint Graph (constraint_graph.html)...")
    net = Network(notebook=False, height="500px", width="100%")
    
    # Add Nodes (People)
    for var in csp.variables:
        net.add_node(var, label=var, color='#4a90e2', title=f"Person {var}")

    # Add Edges
    # All diff constraints in gray
    friction_pairs = [('A', 'B'), ('B', 'E'), ('B', 'C')]
    
    for A in csp.variables:
        for B in csp.neighbors[A]:
            # no duplicate edges for undirected graph 
            if A < B: 
                if (A, B) in friction_pairs or (B, A) in friction_pairs:
                    net.add_edge(A, B, color='red', width=3, title="Conflict!")
                else:
                    net.add_edge(A, B, color='#cccccc', title="AllDiff")
    
    net.show("constraint_graph.html", notebook=False)
    print("Graph generated.")

def check_ac3_impact(csp):
    print("\nStep 4: AC-3 Analysis")
    
    # domains before AC3
    domains_before = {v: list(csp.choices(v)) for v in csp.variables}
    
    print("Running AC3...")
    AC3(csp)
    
    domains_after = csp.curr_domains
    
    changed = False
    print(f"{'Variable':<10} | {'Before':<20} | {'After':<20}")
    print("-" * 55)
    for v in csp.variables:
        b_len = len(domains_before[v])
        a_len = len(domains_after[v]) if domains_after else len(domains_before[v])
        if b_len != a_len:
            changed = True
        print(f"{v:<10} | Size: {b_len:<14} | Size: {a_len:<14}")
        
    if not changed:
        print("\nResult: domains did NOT change.")
        print("Reason: In a circular arrangement with no fixed starting point, \n any person can technically start in any chair. \n xause constraints are relative, not absolute. \n so other solutions are possible")
    else:
        print("\nResult: Domains were pruned.")

def solve_problem(csp):
    #backtracking
    print("\nStep 5: Backtracking Search")
    solution = backtracking_search(csp)
    if solution:
        print("Solution found:", solution)
        # Pretty print
        sorted_sol = sorted(solution.items(), key=lambda x: x[1])
        print("Table Arrangement (Clockwise):")
        for person, chair in sorted_sol:
            print(f"Chair {chair}: {person}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    problem = DinnerSeatingCSP()
    
    #visualize
    visualize_constraints(problem)
    
    # check AC3 with copy
    problem_for_ac3 = copy.deepcopy(problem)
    check_ac3_impact(problem_for_ac3)
    
    #solve
    solve_problem(problem)