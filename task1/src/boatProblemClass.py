from src.problemClass import Problem

class boatProblem(Problem):

#goalstate = RRRR, 

    def __init__(self, initial, goal, graph):
      super().__init__(initial, goal)
      self.graph = graph

    def actions(self, A):
      return list(self.graph.origin[A].keys())

    def result(self, state, action):
      #A transition model
      return self.graph.origin[state][action]
      #return self.graph.get(state).get(action)

    def path_cost(self, cost_so_far, A, action, B):
      #An action cost function
      #return cost_so_far + self.graph.get(A, B)

      #load wolf/goat
      if 'crossW' in action or 'crossG' in action:
            cost = 3
      #load cabbage
      elif 'crossC' in action:
          cost = 2
      #boat left/right
      elif 'boatMove' in action: 
          cost = 1
      else: 
          cost = 1 

      return cost_so_far + cost