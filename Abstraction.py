'''Abstraction in Python  involves hiding unnecessary implementation details and showing only the essential features or functionality. 
It simplifies code, improves modularity, 
and helps manage complexity by focusing on what an object does rather than how it does it.
'''
from abc import ABC , abstractclassmethod, abstractmethod

class Vihical:
    @ abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    def engine_stop(self):
        print("Engine Stop.")


class car(Vihical):

    def start_engine(self):
        print("Car engine is start")

    def drive(self):
        print("Car is drive")

    
class bike(Vihical):

    def start_engine(self):
        print("Bike engine is start")

    def drive(self):
        print("Bike is drive")

# Make car object
c1 =car()
c1.start_engine()
c1.drive()
c1.engine_stop()

# make bike object
b1= bike()
b1.drive()
b1.engine_stop()
b1.start_engine()



# project 2
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)