## Polymorphism
"""sumary_line

Polymorphism is core concept in object-oriented programming That allows objects of different classes 
to be treated as objects of a common superclass. It provides a way to perform a single action in different forms.

Polymorphism is typically achieved through method overriding and interfaces

2 Type to achive

1 Type : Method Overriding 

Method overrinding allows a child class to provide a specific 

implemention of a method that is already defined in its parent class
"""
#Base class

class Animal:
    def speak(self):
        return "sound of the animal"
    
## derived class 1

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
print(dog.speak())

cat = Cat()

print(cat.speak())

##  Function That demonstrate polymorphism
def  animal_speak(animal):
    print(animal.speak())

animal_speak(dog)