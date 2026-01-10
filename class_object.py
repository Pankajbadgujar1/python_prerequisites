class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{self.name} say woof')
    
dog1 = Dog("lucky",4)
print(dog1.name)
print(dog1.age)
dog1.bark()

dog2 = Dog("lucy", 7)
print(dog2.name)
print(dog2.age)
dog2.bark()