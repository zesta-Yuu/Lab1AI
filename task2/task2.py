from data.MazeMapData import *
from src.agents import ProblemSolvingMazeAgentBFS
from src.graphClass import Graph

mazeGraph = Graph(graph_dict=MazeData)

agent = ProblemSolvingMazeAgentBFS(
    WorldGraph=mazeGraph, 
    initState='S', 
    goalState=treasureLocation,
    
)


print("Starting run: S -> Closest Treasure -> E")

final_path = agent.run() 

if final_path:
    print("\n\n Best optimal path actions:")
    print(final_path)
else:
    print("\nAgent failed, cant find a complete path.")
