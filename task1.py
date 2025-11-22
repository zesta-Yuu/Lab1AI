from src.CSPS import DinnerSeatingCSP
from src.algorithms import backtracking_search

def solve():
    print("Solving Task 1: Dinner Accommodation (5 people, 6 chairs on the dinning table)...")
    csp = DinnerSeatingCSP()
    
    #use heuristic in algorith file
    solution = backtracking_search(csp)
    
    if solution:
        print("\nSolution Found:")
        # Sort solution by chair #
        sorted_seats = sorted([(p, c) for p, c in solution.items()], key=lambda x: x[1])
        
        # Find empty chair
        filled_chairs = set(solution.values())
        empty_chair = [c for c in range(1, 7) if c not in filled_chairs][0]
        
        print(f"{'Chair':<10} | {'Person':<10}")
        print("-" * 25)
        for p, c in sorted_seats:
            print(f"{c:<10} | {p:<10}")
        print(f"{empty_chair:<10} | (Empty)")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve()