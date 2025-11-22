from queue import Queue
from src.utils import first

def AC3(csp):

    queue = Queue()

    # Initialize the queue with all arcs
    for Xi in csp.variables:
        for Xk in csp.neighbors[Xi]:
            queue.put((Xi, Xk))

    csp.support_pruning()
    checks = 0

    while not queue.empty():
        (Xi, Xj) = queue.get()
        
        revised, checks = revise(csp, Xi, Xj, checks)
        
        if revised:
            if not csp.curr_domains[Xi]:
                return False, checks  # CSP is inconsistent (empty domain)
            
            # If domain changed, re-check neighbors
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.put((Xk, Xi))
                    
    return True, checks 


def revise(csp, Xi, Xj, checks=0):
 
    revised = False
    
    # Iterate over a copy of the domain 
    for x in list(csp.curr_domains[Xi]):
        # Check if there is ANY value y in Xj that supports x
        is_satisfied = False
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                is_satisfied = True
                break
            checks += 1
            
        if not is_satisfied:
            csp.prune(Xi, x)
            revised = True
            
    return revised, checks


# heuristics n selection

def first_unassigned_variable(assignment, csp):
    return first([var for var in csp.variables if var not in assignment])

def unordered_domain_values(var, assignment, csp):
    return csp.choices(var)

#Backtracking Search

def backtracking_search(csp, select_unassigned_variable=first_unassigned_variable, 
                        order_domain_values=unordered_domain_values, 
                        initial_assignment=None): 
    
    if initial_assignment is None:
        initial_assignment = {}
        
    csp.support_pruning()

    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment

        var = select_unassigned_variable(assignment, csp)
        
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)
                
                result = backtrack(assignment)
                if result is not None:
                    return result
                
                csp.unassign(var, assignment)
        return None

    return backtrack(initial_assignment)

