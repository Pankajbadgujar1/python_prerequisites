## Inheritance in python

# Parent class
class Car:
    def __init__(self,windows, doors,enginetype):
        self.windows= windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print(f"The person will drive the {self.enginetype} car")


obj = Car(4,5,'petrol')
print(obj.drive())

class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdirving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdirving = is_selfdirving

    def selfdirving(self):
        print(f"Tesla support selfdriving : {self.is_selfdirving} ")

Tesla1 = Tesla(4,5,"electronic",True)
Tesla1.selfdirving()
Tesla1.drive()


