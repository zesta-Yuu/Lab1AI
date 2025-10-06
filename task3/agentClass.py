
from thingClass import Thing

import collections.abc

class Agent(Thing):

    def __init__(self, program=None):
        self.alive = True
        self.performance = 0
        self.location=None
        #if agent program isnt given
        if program is None or not isinstance(program, collections.abc.Callable):
            print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))

            def program(percept):
                return eval(input('Percept={}; action? '.format(percept)))

        self.program = program
