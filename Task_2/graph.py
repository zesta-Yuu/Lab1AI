import Class_GameOfThronesGraph

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

#Configure your x and y values from the dictionary:
x= list(Class_GameOfThronesGraph.visualisationData.keys())
y=list(Class_GameOfThronesGraph.visualisationData.values())

fig, ax = plt.subplots()

#Create the graph = create seaborn barplot
ax=sns.barplot(x=x,y=y)

#specfiy axis labels
ax.legend(Class_GameOfThronesGraph.legendData)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1.05, 1))
ax.set(xlabel='Houses',
       ylabel='Strength (N family members)',
       title='Strength of GameOfThronesHouses')

plt.xticks(rotation=45)

plt.title("Strength of Game of Thrones Houses")
plt.tight_layout()

#display barplot 
#plt.show()