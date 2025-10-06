
from CompanyEnvironmentClass import CompanyEnvironment
from Task3YourClasses import Student, ITStaff, OfficeManager
from agents import ReflexAgentA2pro
from agentClass import *
if __name__ == "__main__":
     
    ce=CompanyEnvironment() 
    s=Student()
    i=ITStaff()
    o=OfficeManager()
    print("Adding ITStaff")
    
    ce.add_thing(i)
    print("Adding Student")
    ce.add_thing(s)
    print("Adding OfficeManager")
    ce.add_thing(o)

    print("\n Current Locations: ")
    print("IT is located at {}.".format(i.location))
    print("Student is located at {}.".format(s.location))
    print("OfficeManager is located at {}.".format(o.location))

    ce.things
    
    raTask3pro1=Agent(program=ReflexAgentA2pro)
    ce.add_thing(raTask3pro1)
    print("State of the Office Environment: {}.".format(ce.locations))
    print("Agent is located at {}.".format(raTask3pro1.location))
    ce.step()
    ce.run()