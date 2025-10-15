from src.boatProblemSolvingAgentClass import boatProblemSolvingAgent
import collections.abc

class boatProblemSolvingAgentSMART(boatProblemSolvingAgent):
  ##teach added program smth bout brain??
  def __init__(self, initial_state=None, dataGraph=None, goal=None, program=20):
    super().__init__(initial_state,dataGraph,goal)

    self.performance = 20
    #self.last_action_name = "Initial State"
    if program is None or not isinstance(program, collections.abc.Callable):
      print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))

      def program(percept):
        return eval(input('Percept={}; action? '.format(percept)))

    self.program = program

  def search(self, problem):
    seq = self.program(problem)
    solution=self.actions_path(seq.path())
    print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))

    node_solution = [node.state for node in seq.path()]
    print("Node Solution (a sequence of states) from the initial state to a goal: {}".format(node_solution))
    #storing nodes
    self.node_seq = node_solution[1:] 
    return solution
  
  def actions_path(self, p):
    acts=[]
    for n in p:
      acts.append(n.action)
    return acts[1:]