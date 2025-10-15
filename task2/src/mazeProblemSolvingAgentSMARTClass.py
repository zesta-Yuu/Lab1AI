from src.mazeProblemSolvingAgentClass import mazeProblemSolvingAgent
import collections.abc

class mazeProblemSolvingAgentSMART(mazeProblemSolvingAgent):
  def __init__(self, initial_state=None, dataGraph=None, goal=None, program=None):
    super().__init__(initial_state,dataGraph,goal, program=program)

    if program is None or not isinstance(program, collections.abc.Callable):
      print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))

      def program(percept):
        return eval(input('Percept={}; action? '.format(percept)))

    self.program = program


  
  def search(self, problem):
    seq = self.program(problem)
    if seq:
      solution=self.actions_path(seq.path())
      print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))
      return solution, seq
    else:
            return [], None
  
  def actions_path(self, p):
    acts=[]
    for n in p:
      acts.append(n.action)
    return acts[1:]
  

   
  #new method to calc cost to all treaures then get closest
  def find_closest_treasure(self):
  
      treasure_locs = self.goal 
      current_state = self.state
      
      #just a high #
      closest_cost = 1000 
      closest_tnode = None
      
      print("\nFinding the Closest Treasure")

      for treasure, treasure_node in treasure_locs.items():
          print(f"-->Testing path to {treasure} at node {treasure_node}")
          
          #search/formlate from S->treasure
          problem = self.formulate_problem(current_state, treasure_node)
          
          #self.search = sol & seq, only need seq
          _, seq = self.search(problem) 
          
          if seq:
              current_cost = seq.path_cost
              
              print(f"Path Cost of {treasure} is: {current_cost} \n \n") 
           
              #find min cost
              if current_cost < closest_cost:
                  closest_cost = current_cost
                  closest_tnode = treasure_node
                  
      if closest_tnode:
          print(f"\nClosest Treasure: {treasure} is at {closest_tnode} (path cost: {closest_cost})")
      
      return closest_tnode

  #start-> closet treasure -> exit
  def run(self):
          #end/exit
          exit_Node = 'E' 
          
          #closest treasure
          first_goal = self.find_closest_treasure()
          
          if not first_goal:
              print("Agent failed to find a path to any treasure.")
              return []

          #search to first treasure
          print("\n Search 1: Start to closest treasure")
          problem1 = self.formulate_problem(self.state, first_goal)
          
          solution1, _ = self.search(problem1)
          self.seq = solution1
          
          #state = treasure node
          self.state = first_goal 

          #treasure node -> exit
          print(f"\n Search 2: {self.state} to Exit ({exit_Node})")
          problem2 = self.formulate_problem(self.state, exit_Node)
          
          solution2, _ = self.search(problem2)
          ##need .extrend else itll be overwritten
          self.seq.extend(solution2)

          
          #state = exit
          self.state = exit_Node
          
          print("\n Complete solution in seq (Path: S -> T -> E) ")
          return self.seq