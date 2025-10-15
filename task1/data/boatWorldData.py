

boatWorldStates=['wolf','goat', 'cabbage', 'boat'] ##loc wolf, goat, cabbage, boat
agenLocations=['Left','Right']
agentActions=['crossW','crossG', 'crossC','boatMove']

##LLLL, LLLR, LLRL, LLRR, LRLL, LRLR, LRRL, LRRR, RLLL, RLLR, RLRL, RLRR, RRLL, RRLR, RRRL, RRRR
##LLLL, LLRL, LRLL, RLRL,  RLLL,     LRRR, ,LRLR, RLRR, RRLR, RRRR
## doesnt work states: LLLR, LLRR, LRRL, RLLR, RRLL, RRRL 

##loc of states, and current location
LLLL=''.join(map(lambda x: x[0],(agenLocations[0],agenLocations[0],agenLocations[0],agenLocations[0])))
LLRL=''.join(map(lambda x: x[0],(agenLocations[0],agenLocations[0],agenLocations[1],agenLocations[0])))
LRLL=''.join(map(lambda x: x[0],(agenLocations[0],agenLocations[1],agenLocations[0],agenLocations[0])))
RLRL=''.join(map(lambda x: x[0],(agenLocations[1],agenLocations[0],agenLocations[1],agenLocations[0])))
RLLL=''.join(map(lambda x: x[0],(agenLocations[1],agenLocations[0],agenLocations[0],agenLocations[0])))

LRRR=''.join(map(lambda x: x[0],(agenLocations[0],agenLocations[1],agenLocations[1],agenLocations[1])))
LRLR=''.join(map(lambda x: x[0],(agenLocations[0],agenLocations[1],agenLocations[0],agenLocations[1])))
RLRR=''.join(map(lambda x: x[0],(agenLocations[1],agenLocations[0],agenLocations[1],agenLocations[1])))
RRLR=''.join(map(lambda x: x[0],(agenLocations[1],agenLocations[1],agenLocations[0],agenLocations[1])))
RRRR=''.join(map(lambda x: x[0],(agenLocations[1],agenLocations[1],agenLocations[1],agenLocations[1])))

#agentActions=['crossW','crossG', 'crossC','boatMove']
boatWorld = (dict(
    #DDL=dict(Suck=CDL,Left=DDL, Right=DDR),
    LLLL= dict(crossG= LRLR),
    LLRL= dict(crossW=RLRR, crossG=LRRR),
    LRLL= dict(crossW=RRLR, crossC=LRRR, boatMove=LRLR),
    LRLR= dict(crossG=LLLL, boatMove=LRLL),
    LRRR= dict(crossG=LLRL, crossC=LRLL),
    RLLL= dict(crossG=RRLR, crossC=RLRR),
    RLRL= dict(crossG=RRRR, boatMove=RLRR),
    RLRR= dict(crossW=LLRL, crossC=RLLL, boatMove=RLRL),
    RRLR= dict(crossW=LRLL, crossG=RLLL),
    RRRR= dict(crossG=RLRL)
))

keyList = [LLLL, LLRL, LRLL, RLRL, RLLL, LRRR, LRLR, RLRR, RRLR, RRRR]

import random
##loc func rand generation
def boatStatesLocations():
  x = []
  y = []
  n=len(keyList)
  for _ in range(n):
    x.append(random.randint(0, n+1)+100)
    y.append(random.randint(0, n+1)+100)
  zipped = zip(x, y)
  return dict(zip(keyList, zipped))


def getAction(dict):
  edge_weights = {(k, v2) : k2 for k, v in dict.items() for k2, v2 in v.items()}#actions
  return edge_weights
