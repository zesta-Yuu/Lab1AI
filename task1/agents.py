from agentPrograms import *
from agentClass import Agent

from rules import vacuumRules
from rules import actionList
from rules import table


'''Randomly choose one of the actions from the vacuum environment'''
def RandomVacuumAgent():
    return Agent(RandomAgentProgram(actionList))


def TableDrivenVacuumAgent():
     return Agent(TableDrivenAgentProgram(table))
 
 
def ReflexAgent() :
  return Agent(ReflexAgentProgram(vacuumRules,interpret_input,rule_match))


def ReflexAgentA2pro():
    pass
    #your code here
  

