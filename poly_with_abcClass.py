# Abstract Base Class ABC CLASS
from abc import ABC, abstractmethod

#define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## Derived class1 
class Car(Vehicle):
    def start_engine(self):
        return "Car engine Started"
    

# Derived Class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started "

def start_vehicle(vehicle):
    print(vehicle.start_engine())
    


## Create objects of car and motorcycle

car = Car()
Motorcycle = Motorcycle()

start_vehicle(car)