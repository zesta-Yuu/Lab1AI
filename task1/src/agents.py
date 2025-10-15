
# for the Assignment3

from src.PS_agentPrograms import *
from src.boatProblemSolvingAgentSMARTClass import boatProblemSolvingAgentSMART

#def ProblemSolvingBoatAgentBFS(initState='LLLL', boatWorldGraph, goalState='RRRR'):
def ProblemSolvingBoatAgentBFS(boatWorldGraph, initState='LLLL', goalState='RRRR'):
    return boatProblemSolvingAgentSMART(initState,boatWorldGraph,goalState,BestFirstSearchAgentProgram())

