# Operation overloading

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,another):
        return Vector(self.x + another.x, self.y + another.y)
        

    def __sub__(self,another):
        return Vector(self.x - self.x , self.y - self.y)

    
    
    def __mul__(self,another):
        return Vector(self.x * self.x , self.y * self.y)


    def __eq__(self,another):
        return Vector(self.x == self.x , self.y == self.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


#create objects
v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1)
print(v2)
print(v1+v2)