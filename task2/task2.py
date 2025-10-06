from CatFriendlyHouseEnvClass import *
from agents import *

if __name__ == "__main__":
    
    #init enviroment
    house = CatFriendlyHouseEnvironment()
    cat_agent = TableDrivenAgent()
    
    house.add_thing(cat_agent, start_performance=0)

    print("\n--- CAT-FRIENDLY HOUSE SIMULATION (Table-Driven agent!) ---")
    print(f"Starting Agent: {cat_agent.show_state()}")
    house.print_status()
    print("-" * 50)

    house.run()
    
    print("\n Simulation END")
    print(f"Final Agent State: {cat_agent.show_state()}")