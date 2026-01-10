"""
Magic method 

Magic methods are predefined methods in Python that you can override to change the behavior 
of your objects. 

These methods enable you to define the behavior of objects for built-in operations, such as arithmetic operations , comparisons, and more


Some common magic methods are: 
__init__: Initializes a new instance of a class
__str__:  Returns a string representation of an object
__repr__:  Return an official string representation of an object.
__len__:  Retruns th lenght of an object.
__getitem__: Gets an item from a container.
__setitem__: Set an item in a container


\
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"


    def __repr__(self):
        return f"Person (name={self.name}, age={self.age})"

obj = Person("Pankaj",23)

print(obj)
print(repr(obj))

#print(dir(obj))

