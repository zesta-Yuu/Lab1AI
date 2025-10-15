import streamlit as st
import os
from data.boatWorldData import *
from src.BoatGraphClass import BoatGraph
from src.agents import ProblemSolvingBoatAgentBFS
from src.naigationEnvironmentClass import NavigationEnvironment

#init images
imageDir= "images"
boatObjects = ["wolf", "goat", "cabbage", "boat"]
images = {name: os.path.join(imageDir, f"{name}.png") for name in boatObjects}

#display images
def display_state(state):
    st.subheader(f"Current State: {state}")
    left_col, river_col, right_col = st.columns([4,1,4])

    with left_col:
        #**bold**
        st.markdown("### Left Bank")
        for obj, pos in zip(boatObjects, state):
            if pos == "L":
                st.image(images[obj], caption=obj.capitalize(), width=70)

    with river_col:
        st.markdown("### River")

    with right_col:
        st.markdown("### Right Bank")
        for obj, pos in zip(boatObjects, state):
            if pos == "R":
                st.image(images[obj], caption=obj.capitalize(), width=70)

# run agent step
def AgentStep():
    e = st.session_state["env"]
    a = st.session_state["agent"]

    if e.is_agent_alive(a):
        e.step()

        #save new state
        current_state = getattr(a, "state", None)
        if isinstance(current_state, (list, tuple)):
            current_state_str = "".join(current_state)
        else:
            current_state_str = str(current_state)

        st.session_state["state_sequence"].append(current_state_str)
        st.session_state["last_state"] = current_state_str

        # Display results and visualization **once**
        st.success(f"Agent now at: {current_state_str}")
        st.info(f"Agent performance: {a.performance}")
        display_state(current_state_str)

    else:
        if a.state == a.goal:
            st.success(f"Agent reached goal: {a.state}")
        else:
            st.success(f"Agent at {a.state} and simulation is complete.")

def main():
    st.title("Resolving Wolf, Goat, and Cabbage Problem..")
    st.markdown("Each state shows where (WGCB): wolf, goat, cabbage, and boat are (Left/Right bank).")


    if "initialized" not in st.session_state:
        st.session_state["initialized"] = True
        st.session_state["state_sequence"] = []
        st.session_state["last_state"] = None

        boat_world_graph = BoatGraph(graph_dict=boatWorld)
        env = NavigationEnvironment(navGraph=boat_world_graph)
        agent = ProblemSolvingBoatAgentBFS(boatWorldGraph=boat_world_graph)
        env.add_thing(agent)

        st.session_state["env"] = env
        st.session_state["agent"] = agent

    #agent button
    if st.button("Run One Agent Step", use_container_width=True):
        AgentStep()

    # dis init state if steps ran=0
    if not st.session_state["state_sequence"]:
        initial_state = getattr(st.session_state["agent"], "state", None)
        if isinstance(initial_state, (list, tuple)):
            initial_state_str = "".join(initial_state)
        else:
            initial_state_str = str(initial_state)
        st.session_state["last_state"] = initial_state_str
        display_state(initial_state_str)

    #print state seq
    if st.session_state["state_sequence"]:
        st.markdown("**State sequence so far:**")
        st.write(" -> ".join(st.session_state["state_sequence"]))

if __name__ == "__main__":
    main()
