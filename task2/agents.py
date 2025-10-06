from agentPrograms import *
from AgentCat import *

from rules import table
def TableDrivenAgent():
    return AgentCat(TableDrivenAgentProgram(table))
