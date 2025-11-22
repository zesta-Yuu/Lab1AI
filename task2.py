from src.CSPS import SudokuCSP
from src.algorithms import backtracking_search, AC3

def solve_task2():
    print("Setting up Task 2: Asterisk Sudoku...")

    grid_str = (
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

    asterisk_indices = []
    clean_grid = ""

    for index, char in enumerate(grid_str):
        if char == '*':
            asterisk_indices.append(index)
            clean_grid += '.'  
        else:
            clean_grid += char

    print(f"Found {len(asterisk_indices)} asterisk cells at indices: {asterisk_indices}")
  
    csp = SudokuCSP(clean_grid, asterisk_indices=asterisk_indices)
    
    #solve with Backtracking
    print("Running backtracking search...")
    AC3(csp) 
    solution = backtracking_search(csp)

    #output
    if solution:
        print("\nSolution Found!\n")
        print_board(solution, asterisk_indices)
    else:
        print("No solution found.")

def print_board(solution, stars):
    print("+" + "---+"*9)
    for r in range(9):
        row_str = "|"
        for c in range(9):
            idx = r * 9 + c
            val = solution.get(idx, '.')
            # print n mark the asterisk cells 
            marker = "*" if idx in stars else " "
            row_str += f" {val}{marker}|"
        print(row_str)
        print("+" + "---+"*9)

if __name__ == "__main__":
    solve_task2()