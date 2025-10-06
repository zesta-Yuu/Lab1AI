from environmentClass import Environment
from FoodClass import Milk, Sausage
import random
from locations import *
from AgentCat import *

class CatFriendlyHouseEnvironment(Environment):
  def __init__(self):
      super().__init__()
      
      #rand food rooms
      rooms = [LOC_A, LOC_B]
      random.shuffle(rooms)
      
      self.status = {
          rooms[0]: [Milk()],
          rooms[1]: [Sausage()]
      }
          
  def print_status(self):
      #print room content
      print("-" * 35)
      for room in LOCATIONS:
          items = self.status.get(room, [])
          print(f"  Room {room}: {items}")
      print("-" * 35)

  def percept(self, agent):
      #return whats in room
      location = agent.location
      items = self.status.get(location, [])
      
      if not items:
          status = 'Empty'
      else:
          item = items[0]
          if isinstance(item, Milk):
              status = 'MilkHere'
          elif isinstance(item, Sausage):
              status = 'SausageHere'
          else:
              status = 'Empty'
      return (location, status)

  def execute_action(self, agent, action):


      # If table fails, skip step
      if action is None:
          print("Cat did nothing (No action in Table specified for the sequnce!!")
          return

      if agent.alive:
          if action == 'MoveRight':
              if agent.location == LOC_A:
                  agent.location = LOC_B
                  agent.performance -= 1
                  print(f"Cat moves Right from {LOC_A} to {LOC_B} Performance -1.")
              else:
                  print(f"Cat can't move right since its already at {LOC_B}.")
                  
          elif action == 'MoveLeft':
              if agent.location == LOC_B:
                  agent.location = LOC_A
                  agent.performance -= 1
                  print(f"Cat moves Left from {LOC_B} to {LOC_A} Performance -1.")
              else:
                  print(f"Cat can't move right since its already at {LOC_A}.")
          

          elif action == 'Drink':
              item = self.status.get(agent.location, [None])[0]
              
              if item and agent.drink(item):
                  self.status[agent.location].remove(item)
                  print("Updating the house, Milk was consumed")
                  self.print_status() 
              else:
                  print(f"Action failed")
              
          elif action == 'Eat':
              item = self.status.get(agent.location, [None])[0]

              if item and agent.eat(item):
                  self.status[agent.location].remove(item)
                  print("Updating the house, Sausage was consumed")
                  self.print_status() 
              else:
                  print(f"Action failed")

          self.update_agent_alive(agent)