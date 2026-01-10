"""
Encapulation 
 Encapulation is the concept of wrapping data (variables) and 
methods (functions) together as a single unit. It restricts direct
access to some of the objects components , which is a means of preventing accidental
interference and misuse of the data 

Class is the best example of the encapulation

access modifier in python 
1) Public - instance veriables are public veriables
2) protected  -> it start wit single underscore _ ex. _name 
                This veriable can not access outside from class but can access from derived class (using inheritance)
3) Private -> its start with __ ex. __age 



"""

## Encapulation with getter and setter

class Person:
    def __init__(self,name, age):
        self.__name = name ##Private access modifier or variable
        self.__age = age ## Private variable

    #getter method for name
    def get_name(self):
        return self.__name

    #setter method for name
    def set_name(self):
        self.__name = name

    #getter method for age
    def get_age(self):
        return self.__age

    #setter method for age
    def set_age(self,age):
        if age >0:
            self.__age = age
        else:
            print("Age cannot be negative.")
        

person = Person("krisha",34)

# Access and modify private variable using getter and setter 
print(person.get_age())
person.set_age(35)
print(person.get_age())