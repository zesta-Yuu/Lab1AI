
from src.problemClass import Problem
from src.utils import count

class CSPBasic(Problem):
    def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0
        
        self._pruned = []

    def support_pruning(self):
        """Make sure we can prune values from domains. 
        (We want to pay for this only if we use it.)"""
        if self.curr_domains is None:
            # make a shallow copy of each domain list so lists are not shared
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}
            self._pruned = []

    def prune(self, var, value):
        """Rule out var=value. Remove only if present and record the pruning."""
        if self.curr_domains is None:
            # If someone calls prune before support_pruning, create curr_domains
            self.support_pruning()
        if value in self.curr_domains[var]:
            self.curr_domains[var].remove(value)
            self._pruned.append((var, value))
        # If value wasn't present, do nothing (avoid exceptions)

    def restore_pruned(self):
        """Restore all pruned values into curr_domains (useful for debugging/reset)."""
        for (v, val) in self._pruned:
            if val not in self.curr_domains[v]:
                self.curr_domains[v].append(val)
        # Clear pruned list after restore
        self._pruned = []


class CSP(CSPBasic):
    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""

        # Subclasses may implement this more efficiently
        def conflict(var2):
            return var2 in assignment and not self.constraints(var, val, var2, assignment[var2])

        return count(conflict(v) for v in self.neighbors[var])

    def display(self, assignment):
        """Show a human-readable representation of the CSP."""
        print(assignment)

    def choices(self, var):
        """Return all values for var that aren't currently ruled out."""
        return (self.curr_domains or self.domains)[var]

    def LCV_conflicts(self, var, val, assignment):
        count_conflict = 0
        for n in self.neighbors[var]:
            if n not in assignment and self.curr_domains:
                for n_val in self.curr_domains[n]:
                    if not self.constraints(var, val, n, n_val):
                        count_conflict += 1
        return count_conflict
