from abc import ABC, abstractmethod
import random

class Compartment(ABC):
    @abstractmethod
    def notice(self):
        pass

class FirstClass(Compartment):
    def notice(self):
        print("Welcome to First Class compartment")
    
class Ladies(Compartment):
    def notice(self):
        print("Welcome to Ladies compartment")
    
class General(Compartment):
    def notice(self):
        print("Welcome to General compartment")

class Luggage(Compartment):
    def notice(self):
        print("Welcome to Luggage compartment")

class TestCompartment():
    def main(self):
        compartments =[None]*10

        for i in range(10):
            num = random.randint(1,4)

            if num == 1:
                compartments[i] = FirstClass()
            elif num == 2:
                compartments[i] = Ladies()

            elif num == 3:
                compartments[i] = General()
            else:
                compartments[i] = Luggage()

        for comp in compartments:
            comp.notice()
    
passenger = TestCompartment()
passenger.main()


