from src.BoatGraphClass import BoatGraph
from data.boatWorldData import *
from src.agents import ProblemSolvingBoatAgentBFS
from src.naigationEnvironmentClass import NavigationEnvironment
#from PS_agentPrograms import BestFirstSearchAgentProgram


boat_world_graph = BoatGraph(graph_dict=boatWorld)
agent = ProblemSolvingBoatAgentBFS(boatWorldGraph=boat_world_graph)

print(f"Initial state: {agent.state}")
print(f"Goal state: {agent.goal}")

agent(agent.state) 

##agent.seq =actionlist
if not agent.seq:
    print("Search failed. No solution found.")
else:
    boat_env = NavigationEnvironment(navGraph=boat_world_graph) 
    boat_env.add_thing(agent) 

    print("\n Starting Simulation")
    # Run env based on sol step len
    # Each step calls agent.seq.pop(0) and action= plsyed.
    boat_env.run(steps=len(agent.seq)) 

    print("\n Simulation Complete ")
    print(f"Final Agent Performance: {agent.performance}")

