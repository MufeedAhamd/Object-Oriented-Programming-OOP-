''' Object Oriented Programming (OOP)'''

# Class : A class is blueprint or template for creating objects.
# Object : An object is an instance of class , representing the real world entity.

# Class id define by class keyword

class car:

    # constructor : Automatically called when object is created 
    def __init__(self , brand , color):  
        self.brand = brand
        self.color = color
        print("This is class of car") 

    
    def fea(self): # method 
        print(f"My car brand name is : {self.brand}")
        print(f"My car  color is :{self.color} ")

c1 =car("Honda","Blue") # Making an object of class car
c1.fea()  # Calling the method of class


#  Made a class that calculate basic calculation

class calculation:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        print("This class made for basic calculate.")

    def oper(self):
        print(f"Addition of {self.a} and {self.b} is : {self.a + self.b}")
        print(f"Subtraction of {self.a} and {self.b} is : {self.a - self.b}")
        print(f"Multipication of {self.a} and {self.b} is : {self.a * self.b}")
        print(f"Division of {self.a} and {self.b} is : {self.a / self.b}")

a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))
c1 = calculation(a,b)
print("Number 1 is ",c1.a)
print("Number 2 is ",c1.b)
c1.oper()


# Make classs that calculate student result

class student:
    def __init__(self ,name, English, Hindi,Math, Science,GK):
        self.name = name
        self.english = English
        self.hindi = Hindi
        self.math = Math
        self.science = Science
        self.gk = GK
    
    def grade(self):

        print("Student Marks :")
        print(f"{self.name} got {self.english} marks in English")
        print(f"{self.name} got {self.hindi} marks in Hindi")
        print(f"{self.name} got {self.math} marks in Math")
        print(f"{self.name} got {self.science} marks in Science")
        print(f"{self.name} got {self.gk} marks in GK")

        Total = self.english+self.hindi+self.math+self.science+self.gk
        per = (Total / 500) *100
        print(f"{self.name} got {Total} Out of 500")

        if per > 90 :
            print(f"{self.name} got A+ grade in exam ")
        elif per >= 75 and per <=90:
            print(f"{self.name} got A grade in exam.")
        elif per >= 60 and per <=74:
            print(f"{self.name} got B grade in exam.")
        elif per >= 50 and per <=59:
            print(f"{self.name} got C grade in exam.")
        elif per >=40 and per <=49:
            print(f"{self.name} got D grade in exam.")
        else:
            print("Fail ")

name = input("Enter the sudent name :")
english = int(input("Enter Student marks of English :"))
hindi = int(input("Enter Student marks of Hindi :"))
math = int(input("Enter Student marks of Math :"))
science = int(input("Enter Student marks of science :"))
gk  = int(input("Enter Student marks of GK :"))

s1 = student(name, english,hindi,math,science,gk)
s1.grade()