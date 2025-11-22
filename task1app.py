import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from src.CSPS import DinnerSeatingCSP
from src.utils import first

def backtracking_search_generator(csp):

    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        
        # Select unassigned var
        var = first([v for v in csp.variables if v not in assignment])
        
        for value in csp.choices(var):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)
                
                yield assignment
                
                yield from backtrack(assignment)
                
                if len(assignment) == len(csp.variables) and \
                   all(csp.nconflicts(v, assignment[v], assignment) == 0 for v in assignment):
                    return

                csp.unassign(var, assignment)
                yield assignment 
        return None

    csp.support_pruning()
    yield from backtrack({})

def plot_table(assignment):
    """Draws a round table with chairs"""
    fig, ax = plt.subplots(figsize=(5, 5))
    
    #draw table
    circle = plt.Circle((0, 0), 0.7, color='#d4a373', zorder=1)
    ax.add_artist(circle)
    ax.text(0, 0, "Dinner\nTable", ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Chair coordinates (circular)
    num_chairs = 6
    chairs_x = []
    chairs_y = []
    
    # Reverse assign: Chair ID -> Person
    chair_map = {v: k for k, v in assignment.items()}
    
    for i in range(num_chairs):
        # 1 at top (pi/2), clockwise
        angle = np.pi/2 - (2 * np.pi * i / num_chairs)
        x = np.cos(angle)
        y = np.sin(angle)
        
        chair_num = i + 1
        occupant = chair_map.get(chair_num, "?")
        
        # Draw Chair Marker
        chair_color = '#90be6d' if occupant != "?" else '#e0e0e0'
        chair_circle = plt.Circle((x, y), 0.2, color=chair_color, zorder=2)
        ax.add_artist(chair_circle)
        
        # Text
        label = f"{chair_num}\n{occupant}"
        ax.text(x, y, label, ha='center', va='center', zorder=3, fontsize=10, fontweight='bold')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    return fig

# streamlit

st.title(" Dinner Seating CSP Visualizer")

st.markdown("""
**Constraints:**
1. A ≠ B (Conflict)
2. B ≠ E (Conflict)
3. B ≠ C (C is Manager)
4. All must sit in distinct chairs.
""")

if st.button("Start Backtracking Search"):
    csp = DinnerSeatingCSP()
    
    # Create a placeholder for the plot
    plot_placeholder = st.empty()
    status_placeholder = st.empty()
    
    solver = backtracking_search_generator(csp)
    
    step_count = 0
    
    # Iterate through solver steps
    for state in solver:
        step_count += 1
        status_placeholder.text(f"Step: {step_count} | Assigned: {len(state)}/5")
        
        fig = plot_table(state)
        plot_placeholder.pyplot(fig)
        plt.close(fig)
        
        # Slow down animation
        time.sleep(0.3)
        
    status_placeholder.success("Search Complete!")