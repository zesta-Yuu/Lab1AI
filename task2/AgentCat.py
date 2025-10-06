from agentClass import *
from FoodClass import *

class AgentCat(Agent):
    def __init__(self, program=None):
        super().__init__(program)
        
    def eat(self, food_instance):
        if isinstance(food_instance, Sausage):
            gain = food_instance.calories / food_instance.weight
            self.performance += gain
            print(f"Cat EATS {food_instance}. Performance: +{gain:.2f}")
            return True
        else:
            print(f"Cat attempts to EAT, but item is not a Sausage.")
            return False

    def drink(self, food_instance):
        if isinstance(food_instance, Milk):
            gain = food_instance.calories / food_instance.weight
            self.performance += gain
            print(f"Cat DRINKS {food_instance}. Performance: +{gain:.2f}")
            return True
        else:
            print(f"Cat attempts to DRINK, but item is not Milk.")
            return False

    def show_state(self):
        return f"Cat (P: {self.performance:.2f}, Loc: {self.location})"

    def __repr__(self):
        return self.show_state()
