from abc import ABC, abstractmethod

class Transport(ABC): #
    @abstractmethod
    def move(self): #
        pass

class Bus(Transport): #
    def move(self):
        return "Driving on the road"

class Train(Transport): #
    def move(self):
        return "Riding on the rails"

# Objects are accessed polymorphically
vehicles = [Bus(), Train()]
for vehicle in vehicles:
    print(vehicle.move())
