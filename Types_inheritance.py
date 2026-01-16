''' Types of Inheritance :

 1 . Multiple Inheritance
 2 . Mutilabel Inheritance  
 
 '''




''' Multiple inheritancen
One class can inherit multiple calss properties '''

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class employe:
    def __init__(self, department, salary):
        self.department = department
        self.salary = salary


# Multiple Inheritance: inheriting from both person AND employe
class gender(person, employe):
    def __init__(self, name, age, dept, salary, gen):
        # Call each parent's constructor explicitly for multiple inheritance
        person.__init__(self, name, age)
        employe.__init__(self, dept, salary)
        self.gen = gen

    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")
        print(f"Gender : {self.gen}")

# Creating the object
m = gender("abc", 23, "it", 25000, "male")
m.info()


'''  Multilabel Inheritance 
Classes can inheritance Class in label by label
 
'''
class Car:
    def __init__(self,name,price ):
        self.name = name 
        self.price = price

    def start(self):
        print("Car is start.")

    def stop(self):
        print("Car is stop.")

class car_type(Car): # Car type inherit car properties
        def __init__(self, name, price,type,f_type):
            super().__init__(name, price)
            self.type = type
            self.f_type = f_type


class brand(car_type): # bran inherit Car type properties
    def __inti__(self , name , price, type , f_type):
        super().__init__(name,price, type, f_type)

    def detail(self):
        print(f"Car name : {self.name}")
        print(f"Car Price : {self.price}")
        print(f"Car Type : {self.type}")
        print(f"Fual Type  : {self.f_type}")

#  create object 

# object 1
audi = brand("Audi",800000,"Manual","Petrol")
audi.detail()
audi.start()
audi.stop()

# object 2
BMW = brand("BMW",1000000,"Autometic","Patrol")
BMW.detail()
BMW.start()
BMW.stop()

# object 3
tata = brand("Tata",500000,"Manual", "CNG")
tata.detail()
tata.start()
tata.stop()
    

# program 2
class person:
    def __init__(self,name):
        self.name = name

class employe(person):
    def role(self):
        print(f"{self.name} is a Employee")

class manager(employe):
    def department(self,dept):
        print(f"{self.name} is Manager of {dept}")

m1= manager("Mufeed")
m1.role()
m1.department("HR")

    
