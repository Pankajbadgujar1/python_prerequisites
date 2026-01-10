
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)  ## we use this type because we inherite child from multiple parent class
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} say woof"

# Create an object of Dog class

dog = Dog("Mukesh","Pankaj")
dog.speak()
