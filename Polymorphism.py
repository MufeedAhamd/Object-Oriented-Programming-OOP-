'''Polymorphism means "many forms". 
It refers to the ability of an entity (like a function or object) to perform different actions based on the context.

Technically, in Python, polymorphism allows same method, function or operator to behave differently depending on object it is working with. 
This makes code more flexible and reusable
'''

# Method Overriding


class Animal:
    def speak(self):
        return "Some natural noise"
    
class cat(Animal):
    def speak(self):
        return " Cat speak meao "
    
class dog:
    def speak(self):
        return "Dog barks"
    
class loin:
    def speak(self):
        return "Lion roar"
    
l = loin()
print(l.speak())

d = dog()
print(d.speak())

c = cat()
print(c.speak())


# Area 
class shape:
    def area(self):
        return "Shape have some area"
    
class circle(shape):
    def __init__(self, redius):
        self.r = redius
        
    def area(self):
        return "Area of circle",3.14 *self.r*self.r
    
class rectangle(shape):
    def __init__(self, height,weight):
        self.h = height
        self.w = weight
    def area(self):
        return "Area of Rectangle",self.h*self.w

class squar(shape):
    def __init__(self , side):
        self.s = side
    def area(self):
        return "Area of Square", self.s*self.s
    
s = shape()
print(s.area())

c = circle(7)
print(c.area())

r = rectangle(8,6)
print(r.area())

s = squar(6)
print(s.area())




        
