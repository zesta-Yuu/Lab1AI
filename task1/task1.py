
from CrazyHouseClass import *
from agents import *

if __name__ == "__main__":
    
    #environment
    house = CrazyHouseEnvironment()
    # 2. making the agent
    cat_agent = RandomVacuumAgent()
    
    # 3. Add agent to enviromnnet
    house.add_thing(cat_agent, start_performance=10)

    print("--- STARTING CRAZY HOUSE GAME ---")
    print(f"Cat starting in Room: {cat_agent.location}")
    print(f"Initial House Contents (Room: [Items]):")
    
    house.print_layout()
    
    print("-" * 35)

    #will only run for 10 steps
    house.run(steps=10)
    
    print("\n GAME END ")
    print(f"Final Cat's Points/Performance: {cat_agent.performance}")
