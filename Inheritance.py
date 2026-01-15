'''Inheritance is a fundamental concept in object-oriented programming (OOP) 
that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). 
'''

#  Single label inheritance

# shape
class shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def per(self):
        pass

class circul(shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        return ("Area of circule :",3.14*self.r*self.r)
    
    def per(self):
        return "Perimeter  of circule :",2*3.14*self.r
    
class rectangle(shape):
    def __init__(self,h,w):
        self.h =h
        self.w =w

    def area(self):
        return "Area of Rectangle :",self.h * self.w
    
    def per(self):
        return "Perimeter  of Recangle :",2*(self.h+ self.w)
    
class square:
    def __init__(self ,s):
        self.s =s
    
    def area(self):
        return "Area of Square :" , pow(self.s,2)
    
    def per(self):
        return "Perimeter  of Square :",4*self.s

    
# Make object of Circule class
c1 = circul(5)
print(c1.area())
print(c1.per())
print()  # 


# Make object of Rectangle class
r1 =rectangle(4,5)
print(r1.area())
print(r1.per())
print()


# Make object of Square class
s1 = square(6)
print(s1.area())
print(s1.per())


# Animal
class animal:
    def __init__(self,name):
        self.name =name

    def info(self):
        print("Animal name :",self.name)

    def speak(self):
        pass

class cat(animal):
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} speak :Meao")

class dog(animal):
    
    def speak(self):
        print(f"{self.name} : barks")


#  Make object of cat
c =cat("serci")
c.info()
c.speak()

# make object of dog
d = dog("devil")
d.info()
d.speak()


# Empoly tha that inherits person
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")

emp = Employee("Sarah")
print("Name:", emp.name)
emp.show_role()