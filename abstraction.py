"""
Abstraction
Abstraction is the concept of hiding the conplex implimentation details and showing only the necessary 
features of an object. This helps in reducing programming conplexity and effert


"""
from abc import ABC,abstractmethod

# abstract base class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is use for dirving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine stared")

def operate_vehicle(vehicle):
    print("Car engine stated")
    vehicle.drive()

car = Car()
operate_vehicle(car)