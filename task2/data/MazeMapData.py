import random

#Dont do dead ends-> already connected
MazeData=dict(
#S=dict(J1=9),
J1=dict(S=9,J2=8, J3=2),
J2 = dict(J1=9),
J3 = dict(J7=4, J4=4),
J4 = dict(J12=2,J6=4),
##I removed J5/J8
##J5 = dict(),
#J6 = dict(),
J7 = dict(J10=2, J9=4, J3=4),
##J8 = dict(),
J9 = dict(J7=4),
J10 = dict(J11=3, J16=2, J7=2),
J11 = dict(J10=3),
J12 = dict(J13=3, J14=2),
#J13 = dict(),
J14 = dict(J17=2, J15=4),
J15 = dict(J22=6, J14=4, J16=4),
J16 = dict(J19=2, J15=4),
J17 = dict(J18=6, J24=5),
#J18 = dict(),
J19 = dict(J20=6, J23=5),
#J20 = dict(),
#J21 = dict(),
J22 = dict(J15=6, J23=2),
J23 = dict(E=7, J22=2,J19=5),
J24 = dict(J21=6, J22=2, J17=5)
#E=dict()
)

##accidentally started 3 spaces up
"""
MazeLocations = dict(
S=(0,3),
J1 = (9,3),
J2 = (16,3),

J3 = (9,5),
J4 = (5,5),
J7 = (13,5),

#J5 = (),
J6 = (2,8),
#J8 = (),
J9 = (16,8),

J10 = (13,7),
J11 = (10,7),
J12 = (5,7),
J13 = (8,7),

J14 = (5,9),
J15 = (9,9),
J16 = (13,9),

J17 = (5,11),
J19 = (13,11),

J18 = (2,10),
J20 = (16,10),

J21 = (2,15),
J22 = (9,15),
J23 = (11,15),
J24 = (7,15),
E=(15,18)
)
"""

MazeLocations ={
"S":[0,3],
"J1": [9,3],
"J2": [16,3],

"J3": [9,5],
"J4": [5,5],
"J7": [13,5],

#J5": [],
"J6": [2,8],
#J8": [],
"J9": [16,8],

"J10": [13,7],
"J11": [10,7],
"J12": [5,7],
"J13": [8,7],

"J14": [5,9],
"J15": [9,9],
"J16": [13,9],

"J17": [5,11],
"J19": [13,11],

"J18": [2,10],
"J20": [16,10],

"J21": [2,15],
"J22": [9,15],
"J23": [11,15],
"J24": [7,15],
"E":[15,18]
}

all_nodes = (
    [f'J{i}' for i in range(1, 25)] +  
    ['S', 'E']                         
    )

all_nodes.remove('J5')
all_nodes.remove('J8')
#treasure cant be at end/start node
all_nodes.remove('S')
all_nodes.remove('E')

rand_loc = random.sample(all_nodes, 4) 

treasure_types = ['gold', 'diamond', 'pizza', 'points']
##gold, diamond, pizza, points/grade

treasureLocation = dict(zip(treasure_types, rand_loc))

