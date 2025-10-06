
from agentClass import Agent
from rules import actionList
from FoodClass import Milk, Sausage
from locations import *
import random

class Environment:
  def __init__(self):
    self.agents = []
  #percept is the ability of agent, 
  def percept(self, agent):
    #Return the percept that the agent sees at this point. (Implement this in derived classes)
    print("I don't know how to percept.")

  def execute_action(self, agent, action):
    #Change the world to reflect this action. (Implement this in derived classes)
    print("I don't know how to execute_action.")

  def default_location(self, thing):
    #Default location to place a new thing with unspecified location.
    return random.choice(LOCATIONS)

  def is_done(self):
    #By default, we're done when we can't find a live agent.
    
    return not any(agent.is_alive() for agent in self.agents)

  def update_agent_alive(self, agent):
        if agent.performance <= 0:
            agent.alive = False
            print(f"!!! {agent.show_state()} is DEAD. GAME OVER !!!")
            
  def step(self):
        # Run the environment for one time step.
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    percept_result = self.percept(agent)
                    action = agent.program(percept_result)
                    
                    # Print status before action execution
                    print(f"\n--- Turn for Agent ---")
                    print(f"Agent (Points: {agent.performance:.2f}, Room: {agent.location}) percepted {percept_result[1]}.")
                    print("Agent decided to: {}.".format(action))
                    
                    actions.append(action)

                else:
                    print("Agent {} is dead.".format(agent))
                    actions.append("")

            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
        else:
          print("There is no one here who could work...")
        return actions

  def run(self, steps=3):
        #Run the Environment for given number of time steps.
        for step in range(steps):
            if self.is_done():
                print("We can't find a live agent. Game over")
                return
            print("step {0}:".format(step+1))
            self.step()

  def add_thing(self, thing, location=None, start_performance=0):
        # Add agent to envi
        if thing in self.agents:
            print("Can't add the same agent twice")
        else:
            # set inital state/ loc
            thing.performance = start_performance
            thing.location = location if location is not None else self.default_location(thing)
            self.agents.append(thing)
