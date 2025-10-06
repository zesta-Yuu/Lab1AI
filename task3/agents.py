from agentPrograms import *
from agentClass import *

from rules import a2proRules


def ReflexAgentA2pro(percepts):

    state = interpret_input_A2pro(percepts)
    
    action = rule_match_A2pro(state, a2proRules)
    return action
