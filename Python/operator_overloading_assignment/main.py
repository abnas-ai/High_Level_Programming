
#create an instance of an operator overloading situation in oop
#extract two points of a coordinate using the  substraction and addition dunder methods

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)
    
    def __sub__(self, another):
        return Coordinates(self.x - another.x, self.y - another.y)
    
p1 = Coordinates(2, 3)
p2 = Coordinates(3, 4)
p3 = p2 + p1
p4 = p2 - p1
print(f"({p3.x}, {p3.y})")
print(f"({p4.x, p4.y})")
        
        