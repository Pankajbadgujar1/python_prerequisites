## Multilevel inheritance 

## base inheritance

## Base class 1
class Animal:
    def __init__(self,name):
        self.name = name


    def speak(self):
        print("Subclass must implement this method ")

## Base class 2
class Pet:
    def __init__(self,owner):
        self.owner = owner


## derived class

class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)  ## we use this type because we inherite child from multiple parent class
        Pet.__init__(self,owner)

    def speak(self):
        print(f"{self.name} say woof")

# Create an object of Dog class

dog = Dog("Rocky","Pankaj")
dog.speak()
print(dog.owner)





