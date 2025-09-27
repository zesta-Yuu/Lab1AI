import Class_GameOfThronesGraph
import networkx as nx
import seaborn as sns
from pyvis.network import Network

g = nx.Graph() # graph initialization



N_houses=0
colorKeys=[]
for house in Class_GameOfThronesGraph.GameOfThronesHouses:
    if house.name!="Include":
        N_houses+=1
        colorKeys.append(house.name)
sns.color_palette("husl", N_houses) # N_houses colors

#print(list(sns.color_palette("husl", N_houses)))
#print(colorKeys)

nodeColors=dict(zip(colorKeys, [tuple(int(c*255) for c in cs) for cs in sns.color_palette("husl", N_houses)]))
#print(nodeColors)


Colors_hex=[]
for key, values in nodeColors.items():
    colour_tuple = values
    Colors_hex.append(f'{colour_tuple[0]:X}{colour_tuple[1]:X}{colour_tuple[2]:X}')
#print(Colors_hex)
hex_nodeColors= dict(zip(colorKeys,Colors_hex))
#print(hex_nodeColors)

for house in Class_GameOfThronesGraph.GameOfThronesHouses:
    if house.name!="Include":
        #add the house's name as a node to the graph g (node's size=strength)
        g.add_node(house.name, size=house.getStrength(), color='#' + hex_nodeColors[house.name])
for house in Class_GameOfThronesGraph.GameOfThronesHouses:
    if house.name!="Include":
        # add each character as a node to the graph g
        for characters in house:    
            g.add_node(characters, color='#' + hex_nodeColors[house.name])
      
"""#used to check code
for node, attributes in g.nodes(data=True): 
    print(f"Node: {node}, Attributes: {attributes}")"""

myEdges=[]

for house in Class_GameOfThronesGraph.GameOfThronesHouses:
    if house.name!="Include":
        for characters in house:
            g.add_edge(house.name,characters, color='#' + hex_nodeColors[house.name])
            myEdges.append((characters,house.name))

"""print("Connections between a House and its family members:") #  to check your code above
for edge in myEdges:
    print(edge)"""

#adds edges from a list
#g.add_edges_from(myEdges) #add edges to our graph g

"""print(list(g.edges))#check the edges in our graph g
print(len(list(g.edges))) # N of edges =89"""

GameOfThronesNet = Network (
                bgcolor ="#242020",
                font_color = "white",
                height = "1000px",
                width = "1000px", #"100%",
                notebook=False,
                cdn_resources = "remote",
                filter_menu=True 
                )

GameOfThronesNet.from_nx(g)  

#print(GameOfThronesNet.nodes)

GameOfThronesNet.show("Lab1_Taks2_GameOfThrones.html",notebook=False)