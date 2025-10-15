
# for the Assignment3

from src.PS_agentPrograms import *
from src.mazeProblemSolvingAgentSMARTClass import mazeProblemSolvingAgentSMART

def ProblemSolvingMazeAgentBFS(initState,WorldGraph,goalState):
    return mazeProblemSolvingAgentSMART(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

