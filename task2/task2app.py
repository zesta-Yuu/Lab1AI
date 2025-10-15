# Import dependencies
import streamlit as st
import streamlit.components.v1 as components 

import networkx as nx 
from pyvis.network import Network 


from src.graphClass import Graph
from data.MazeMapData import *
from src.agents import ProblemSolvingMazeAgentBFS
from src.mazeEnvironmentClass import MazeEnvironment
from src.mazeProblemSolvingAgentSMARTClass import mazeProblemSolvingAgentSMART

# from src.trivialVacuumEnvironmentClass import TrivialVacuumEnvironment
# from src.agents import RandomVacuumAgent

##blue, purple, yellow, blue

def drawBtn(e,a,c):
    option= [e,a,c]
    st.button("Run One Agent's Step", on_click= AgentStep, args= [option])
    
def AgentStep(opt):
    st.header("Resolving maze Navigation Problem ...")
    e, a, c = opt[0], opt[1], opt[2]

    if not st.session_state["clicked"]:
        st.session_state["env"] = e
        st.session_state["agent"] = a
        st.session_state["nodeColors"] = c    

    if e.is_agent_alive(a):
        e.step()
        st.success(f"Agent now at: {a.state}.")
        st.info(f"The Agent goal is: {a.goal} .")
        st.info(f"Current Agent performance: {a.performance}")

        #if state=purple, node = perma blue
        if st.session_state["nodeColors"][a.state] == "purple":
            st.session_state["nodeColors"][a.state] = "blue"
            st.success(f"You found the treasure at {a.state}!")

        #yellow=past nodes except blue
        if st.session_state["nodeColors"][a.state] not in ["blue"]:
            st.session_state["nodeColors"][a.state] = "yellow"

        #orange=current pos
        displayColors = st.session_state["nodeColors"].copy()
        displayColors[a.state] = "orange"

        st.info("State of the Environment:")
        buildGraph(e.status, displayColors) 

    else:
        if a.state == a.goal:
            st.info(f"Agent now at the goal state: {a.state}.")
        else:
            st.error(f"Agent in location {a.state} and it is dead.")
    
    st.session_state["clicked"] = True


    
        
def buildGraph(graphData, nodeColorsDict):
    netmaze = Network(
        bgcolor ="#242020",
        font_color = "white",
        height = "800px",
        width = "100%"
    )

    g = nx.Graph()

    # add nodes with positions
    for node in graphData.nodes():
        x, y = MazeLocations.get(node, [0, 0]) 
        #scaling
        g.add_node(node, color=nodeColorsDict[node], x=x*50, y=-y*50)  

    # add edges
    edges = []
    for node_source in graphData.nodes():
        for node_target, dist in graphData.get(node_source).items():
            if set((node_source,node_target)) not in edges:
                edges.append(set((node_source,node_target)))
    g.add_edges_from(edges)

    #make graph
    netmaze.from_nx(g)
    netmaze.save_graph('L3_MazeMap.html')
    HtmlFile = open('L3_MazeMap.html', 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height=1200, width=1000)

    
    
def makeDefaultColors(dictData):
    nodeColors=dict.fromkeys(dictData.keys(), "white")
    return nodeColors
        

def main():
        
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False
        
    if "env" not in st.session_state:
        st.session_state["env"]=None
        
    if "agent" not in st.session_state:
        st.session_state["agent"]=None
        
    if "nodeColors" not in st.session_state:
        st.session_state["nodeColors"]=None
        
    if not st.session_state["clicked"]:
        # Set header title
        st.header("Problem Solving Agents: Maze Navigation Problem")
        st.header("_Initial Env._", divider=True)
        
        mazeGraph = Graph(MazeData)
        nodeColors=makeDefaultColors(mazeGraph.graph_dict)
        
 
        #find_closest_treasure
        #goalState=treasureLocation

        re=MazeEnvironment(mazeGraph)
        BFSnavAgent2=ProblemSolvingMazeAgentBFS(
                    WorldGraph=mazeGraph, 
                    initState='S', 
                    goalState=treasureLocation)
           
        final_path = BFSnavAgent2.run()

        re.add_thing(BFSnavAgent2)
        st.header("State of the Environment", divider="red")
        nodeColors["S"]="red"
        nodeColors["E"]="green"
        for _, location in treasureLocation.items():
            nodeColors[location] = "purple"
                
        buildGraph(mazeGraph, nodeColors) 
        st.info(f"The Agent in: {BFSnavAgent2.state} with performance {BFSnavAgent2.performance}.")
        st.info(f"The Agent goal is: {BFSnavAgent2.goal} .")
        

        drawBtn(re,BFSnavAgent2,nodeColors)
         
        
    if st.session_state["clicked"]:
        if st.session_state["env"].is_agent_alive(st.session_state["agent"]):
            #st.warning("Agent Step Done!")
            st.success(" Agent is working...")
            drawBtn(st.session_state["env"],st.session_state["agent"], st.session_state["nodeColors"])
    
    
if __name__ == '__main__':
    main()
    
    

