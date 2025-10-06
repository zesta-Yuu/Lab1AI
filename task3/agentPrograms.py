
from Task3YourClasses import *
from locations import *

def interpret_input_A2pro(percept):
  loc, percepts = percept
  #print(percepts,loc, loc_D)
  status='Clear'
  if len(percepts)==0:
    if loc==loc_D:
      status='Last room'
      #print(1)
  else:
    for p in percepts:
      """
      if isinstance(p, OfficeManager):
        return 'Office manager'
      elif isinstance(p, ITStaff):
        return 'IT'
      elif isinstance(p, Student):
        return 'Student'
        """
      if isinstance(p, (OfficeManager, ITStaff, Student)):
        return p.get_package()
  print(status)
  return status

def rule_match_A2pro(state, rules):
  return rules[state]