import random

'''An idea of Random Agent Program is to choose an action at random, ignoring all percepts'''
def RandomAgentProgram(actions):
   return lambda percept: random.choice(actions)

def TableDrivenAgentProgram(table):
    """
    This agent selects an action based on the percept sequence.
    To customize it, provide as table a dictionary of all 
    {percept_sequence:action} pairs.
    """
    percepts = []

    def program(percept):
        percepts.append(percept)
        #print(tuple(percepts))
        action = table.get(tuple(percepts))
        
        if action is None:
          print("Not such percept sequence in my table")

        return action

    return program
  
  
def ReflexAgentProgram(rules,interpret_input,rule_match):
  #This AP takes action based solely on the percept.
    
    def program(percept):
        state = interpret_input(percept)
        action = rule_match(state, rules)
        return action

    return program


def interpret_input(percept):
  loc, status = percept
  return status


def rule_match(state, rules):
  for key in rules:
    if state in key:
      return rules[key]
