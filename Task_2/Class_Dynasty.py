
import jsontest 

class Dynasty:
    def __init__(self,name):
        self._name=name # House name, for.ex."Martell"
        self.characters=[] # Family members ("Doran Martell","Ellaria Sand","Nymeria Sand",...)


    @property
    def name(self): # getter for the private instance attribute _name
        return self._name
       

    @name.setter
    def name(self, value):
         #- should include Validation: Ensure value is not an empty string
        if len(value) != 0:
           self._name = value
      

    def append(self, ch): # to append character to the House (during reading data from JSON-file) 
        #this code will check if character is an instance
      if not isinstance(ch, str):
        raise TypeError("Character must be a string.")
      
      else:
         self.characters.append(ch)


    def __iter__(self): # to loop throw the list of characters via IN operator (for ex. for person in house: ....)
         return iter(self.characters)

    def __contains__(self, ch): # to check if the character belongs to the house (for ex., if person in house ...)
        # return True or False
        for char in self.characters:
           if char==ch:
             return True
        return False
           
    def __str__(self): # to print like print(house) - > displat the house's name
        return f"This is a House of {self.name} \n"
    
    def getStrength(self): # return N of family members in this house (int)
        return len(self.characters)

"""

for data in jsontest.json_data['groups']:
  house=Dynasty(data['name'])
  for character in data['characters']:
    house.append(character)
  print(house)
  print("Our members:")
  for person in house:
    print(person)
  print(f"We have {house.getStrength()} family members!!!")
  """

