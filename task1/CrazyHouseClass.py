from environmentClass import Environment
#from locations import *
import random

class CrazyHouseEnvironment(Environment):
  def __init__(self):
    super().__init__()          
    self.loc_Cat = random.randint(1, 5)
    self.loc_Mouse = random.randint(1, 5)
    self.loc_Dog = random.randint(1, 5)
    self.loc_Milk = random.randint(1, 5)

    if self.loc_Mouse == self.loc_Dog:
      if self.loc_Mouse == 5:
          self.loc_Mouse = 4
      elif self.loc_Mouse == 1:
          self.loc_Mouse = 2
      else:
          self.loc_Mouse = self.loc_Mouse + random.choice([1, -1])

    if self.loc_Milk == self.loc_Mouse:
      self.loc_Milk = 0 #dead room

    self.status = {i: [] for i in range(1, 6)} 

    if self.loc_Dog != 0:
            self.status[self.loc_Dog].append('Dog')
            
    if self.loc_Milk != 0: 
        self.status[self.loc_Milk].append('Milk') 
        
    if self.loc_Mouse != 0: 
        self.status[self.loc_Mouse].append('Mouse')

                  
  #need to over write percept <-mn
  def percept(self, agent):
    #Returns the agent's location, and the location status (what's in the room).
    return agent.location, self.status[agent.location]

  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print("Agent {} is dead. Game over".format(agent))
      print(f"!!! Agent {agent.__class__.__name__} is DEAD (P={agent.performance}). GAME OVER !!!")

  def execute_action(self, agent, action):
    '''Check if agent alive, if so, execute action'''

    if self.is_agent_alive(agent):
        """Change agent's location and/or location's status;
        Track performance."""
        #Each movement -> perfomace= minus 1
        if action == 'MoveRight':
            if agent.location != 5:
              agent.location += 1
              agent.performance -=1
              print(f"The Cat has moved right")
            else:
               print(f"The Cat is in the last room and cant move right")
            self.update_agent_alive(agent)

        elif action == 'MoveLeft':
            if agent.location != 1:
              agent.location -= 1
              agent.performance -=1
              print(f"The Cat has moved left")
            else:
               print(f"The Cat is in the first room and cant move left")
            self.update_agent_alive(agent)

        elif action == 'Eat':
            if 'Mouse' in self.status[agent.location]:
              if agent.performance >= 3:
                self.status[self.loc_Mouse].remove('Mouse')
                self.loc_Mouse = 0 #dead room
                agent.performance += 10  
                print(f"Cat successfully EATS Mouse! Points +10.")
              else:
                print(f"Cat's (current Points={agent.performance}) is too weak to catch Mouse. Needs Points >= 3.")
              self.update_agent_alive(agent)
            else:
              print(f"The cat is hungry but there's no mouse here.")
              

        elif action == 'Drink':
            if 'Milk' in self.status[agent.location]:
               self.status[self.loc_Milk].remove('Milk')
               self.loc_Milk = 0 #dead room
               agent.performance += 5     
               print(f"Cat DRINKS Milk. Points +5.")
               self.update_agent_alive(agent)
            else:
               print(f"The cat is thirsty but there's no milk here.")


        elif action == 'Fight':
            if 'Dog' in self.status[agent.location]: 
              if agent.performance >= 10:
                agent.performance += 20
                self.status[self.loc_Dog].remove('Dog')
                self.loc_Dog = 0 #dead room
                print(f"Cat WON the fight against the Dog! Points +20.")
              else:
                print(f"Cat (Points={agent.performance}) LOST the fight against the Dog. Points -10.")
                agent.performance -= 10
            else:
               print(f"The cat wants to fight but there's no dog here.")
            self.update_agent_alive(agent)

  def default_location(self, thing):
        """Agents start in either location at random."""
        print("Agent is starting in random location...")
        return self.loc_Cat
  
  def print_layout(self):
    for room in range(1, 6):
      items = self.status[room]
      if items:
          print(f"  Room {room}: {items}")
    if self.loc_Milk==0:
        print("The mouse drank the milk")

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print(f"!!! Agent {agent.__class__.__name__} is DEAD (Points={agent.performance}). GAME OVER !!!")
            
    
