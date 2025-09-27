import jsontest
import Class_Dynasty

class GameOfThronesGraph:
    def __init__(self, corpus):
        #initialisation of dictionary that will store all houses.
        self.houses = {}
        #Load the house corpus
        for data_item in corpus:
            # They keys are Houses' (Dynasty) names
            house_name = data_item['name']
            #, the values are Dynasty objects.
            house_object = Class_Dynasty.Dynasty(house_name)

            self.houses[house_name] = house_object

            for character in data_item['characters']:
                house_object.append(character)


    def __iter__(self): # for the case like the following: for house in GameOfThronesHouses:
         return iter(self.houses.values())
            
    def __contains__(self, h): #Check if h (house's name) is a key in dict houses - the house is in the graph
        if h.capitalize() in self.houses:
            return True
        else:
            return False 

corpusData=jsontest.json_data['groups']
GameOfThronesHouses=GameOfThronesGraph(corpusData)
#print(GameOfThronesHouses.__contains__('stark'))
#for house in GameOfThronesHouses:
#  print(house)


visualisationData={}
legendData=[]
for house in GameOfThronesHouses:
  #print(house)
  #print(f"Strength: {house.getStrength()}")
  visualisationData[house.name]=house.getStrength()
  legendData.append(house.name)

#print(visualisationData)
#print(legendData)