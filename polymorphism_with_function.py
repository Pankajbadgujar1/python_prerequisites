class Shape:
    def area(self):
        return "The area of the figure"

#Derived class 1
class Rectange(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height =height

    def area(self):
        return self.width * self.height

#Derived class 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    


## function that demonstrate polymorphism

def print_area(shape):
    print(f" The area is {shape.area()}")


rectange = Rectange(5,4)
circle = Circle(5)

print_area(rectange)
print_area(circle)