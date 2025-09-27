import pandas as pd
from pyvis.network import Network
import numpy as np
#Loading the data
data = pd.read_csv("game-of-thrones-battles.csv")
#data.head()

#data.info()

battles_df=data.loc[:,
                    ['name','attacker_king','defender_king','attacker_size','defender_size']
                    ]
#print(battles_df.head())
#battles_df.info()
sample = battles_df

#remove rows with any missing values (NaN)
#need .copy() or titles fails
battles_df_cleaned=battles_df.dropna().copy()
#battles_df_cleaned.info()

#print(battles_df_cleaned.head(3))

#Output names of attacking kings (without repetitions):
#print(f"Attacking kings: {battles_df_cleaned.attacker_king.unique()}")

#Output names of defending kings (without repetitions):
#print(f"Defending kings: {battles_df_cleaned.defender_king.unique()}")

net5kings = Network(
heading= "Task1. Building Interactive Network of battles of the War of 5",
bgcolor ="#242020",
font_color = "white",
height = "1000px",
width = "100%",
directed = True, # we have directed graphp
notebook=False,
cdn_resources = "remote",
filter_menu=True 
) 

#Define nodes - the list of unique names of all kings. Hint: use Python set to avoid repetitions
#print(sample.head())


#  display lrg char per col
pd.set_option('display.max_colwidth', None)


all_kings = pd.concat([battles_df_cleaned['attacker_king'],battles_df_cleaned['defender_king']])
unique_kings = list(set(all_kings)) #.dropna()

#print(f"Kings list (nodes 'all_kings''): {unique_kings}")
net5kings.add_nodes(unique_kings)
#print(net5kings.nodes)

edges_list = []
for index, row in battles_df_cleaned.iterrows():
    attacker = row['attacker_king']
    defender = row['defender_king']
    edges_list.append((attacker, defender))

# Print edges
#print("Potential Edges of net5kings: \n")
#for edge in edges_list:
    #print(edge)

unique_edges = list(set(edges_list))
#diff from teachers= sets are unordered
#print("Real (unique) directed Edges of net5kings")
#print(unique_edges)

edges_weights = battles_df_cleaned.groupby(['attacker_king','defender_king'])['name'].count()
edges_weights_df = edges_weights.reset_index()
edges_weights_df.rename(columns={'name': 'battle_count'}, inplace=True)
#print(edges_weights_df['battle_count'])

battles_df_cleaned['titles']= (
    #'Number of battles: ' + edges_weights_df['battle_count'].astype(str) + ' Battles ' +
    #names (king 1 vs king2)
    battles_df_cleaned['name'] + '(' +
    battles_df_cleaned['attacker_size'].astype(int).astype(str) + " vs " +
    battles_df_cleaned['defender_size'].astype(int).astype(str) + ')'
)

edges_titles = battles_df_cleaned.groupby(
    ['attacker_king','defender_king']).agg(
        title= ('titles',  ' | ' .join)
    )
#print(edges_titles)

edges_merged = pd.merge(edges_weights_df, edges_titles, on=['attacker_king', 'defender_king'])
#.to_string(index=False) will remove the auto indexing column
#print(edges_merged.to_string(index=False))


edges_merged['formatting'] = (
    'Attacking king: ' + edges_merged['attacker_king'].astype(str) + 
    ', Defending king: ' + edges_merged['defender_king'].astype(str) +
    ', N of battles: ' + edges_merged['battle_count'].astype(str) +
    ', Battles: ' + edges_merged['title']
)

#print(edges_merged['formatting'].to_string(index=False))
#print(f"edges_weights: {edges_weights_df['battle_count'].tolist()}")

#edges_merged_2= edges_merged.copy()

#The edge from Stannis Baratheon to Mance Rayder with weight 1, title: 'Battle of Castle
edges_merged['edge_weights'] = (
    'The edge from: ' + edges_merged['attacker_king'].astype(str) + 
     ' to: ' + edges_merged['defender_king'].astype(str) + 
    ' with weight: ' + edges_merged['battle_count'].astype(str) +
    ', title: ' + edges_merged['title']
)
#print(edges_merged['edge_weights'].to_string(index=False))

# Iterate 
for index, row in edges_merged.iterrows():
    attacker = row['attacker_king']
    defender = row['defender_king']
    weight = row['battle_count']
    title = row['title']

    # Add edge to network
    net5kings.add_edge(
        value=weight, 
        title=title,
        #does even without specification
        arrows = 'to',
        source=attacker, 
        to=defender,
        #optional
        arrowStrikethrough= False
    )
#print(net5kings.get_edges())

#adj list= dict, key= attacker, val = defender
enemies_map = net5kings.get_adj_list()

#color based on enemy count
nodeColors={
0:"blue",
1: "green",
2: "orange",
3: "purple",
4: "gold",
5:"red"
}

for attacker, enemies in enemies_map.items():
    node_value = len(enemies) + 1
    node = net5kings.get_node(attacker)
    node['value']= node_value
    node['color'] = nodeColors.get(node_value)
    #print(f"King: {attacker} has attacked: {defender}, N of enemies: {len(enemies)}, node's value: {node_value}")

#print(net5kings.nodes)

net5kings.show("Lab1_task1_net5kings.html", notebook=False)
