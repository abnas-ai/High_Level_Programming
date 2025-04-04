#Types of polymorphism
#1)Dynamic polymorphism
#2)Operator overloading
#3)Method Overriding
#4)Method overloading


#1. Method overriding

from abc import ABC, abstractmethod
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def  make_sound(self):
        return "Woof!"
    
class  Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
#2 Method overloading
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
    
op1 = MathOperations()
print(op1.add(2, 3))