import random

class Food:
    #nase class
    def __init__(self, weight, calories):
        self.weight = weight
        self.calories = calories
        
    def __repr__(self):
        # class name + properties
        return f'<{self.__class__.__name__} W:{self.weight} C:{self.calories}>'

class Milk(Food):

    def __init__(self, weight=None):
        #rand weight
        weight = weight if weight is not None else random.randint(3, 11)
        calories = int (weight + 0.7)
        super().__init__(weight, calories)

class Sausage(Food):
    
    def __init__(self, weight=None):
        #rand weight
        weight = weight if weight is not None else random.randint(8, 17)
        calories = int (weight * 0.7)
        super().__init__(weight, calories)
