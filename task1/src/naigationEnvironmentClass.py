from src.environmentClass import Environment


class NavigationEnvironment(Environment):
  def __init__(self, navGraph):
    super().__init__()
    self.status = navGraph
    

  def percept(self, agent):
    #Returns the agent's location, and the location status (Dirty/Clean).
    return agent.state

  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print("Agent {} is dead.".format(agent))
    elif agent.state==agent.goal or len(agent.seq)==0:
      agent.alive = False
      if len(agent.seq)==0:
        print("Agent reached all goals")
      else:
        print(f"Agent reached the goal: {agent.goal}")
      

  def execute_action(self, agent, action, next_state):
    '''Check if agent alive, if so, execute action'''
    if self.is_agent_alive(agent):
        """Change agent's location -> agent's state;
        Track performance."""
        #agent.state=agent.update_state(agent.state, action)
        agent.state = next_state
        #action2= agent.seq = list(agent.seq[1])
        if action== 'crossW' or action== 'crossG':
          cost= 3
        elif action=='crossC':
          cost= 2
        else:
          cost= 1
        #agent.seq = list(agent.seq[0])
        agent.performance-=cost

        print(f"Agent in {agent.state} with cost = {cost} and performance = {agent.performance}")
        self.update_agent_alive(agent)

        
  def step(self):
    if not self.is_done():
        actions = []
        next_states=[]
        for agent in self.agents:
          if agent.alive:
            #with agent.state because for PS Agent we don't need to percive
            if agent.seq:
                action = agent.seq.pop(0)
                next_state = agent.node_seq.pop(0)
            print("Agent decided to do {}.".format(action))
            actions.append(action)
            next_states.append(next_state)
          else:
            actions.append("")
            
        for (agent, action, next_state) in zip(self.agents, actions,next_states):
          self.execute_action(agent, action,next_states)
    else:
        print("There is no one here who could work...")
    