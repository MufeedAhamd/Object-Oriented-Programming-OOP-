'''Encapsulation means hiding internal details of a class and only exposing what’s necessary.
It helps to protect important data from being changed directly and keeps the code secure and organized'''

#  That achive by access specifier

# Public : By default all member or method are public.
# Protected : achive by (_) single underscore . only access in class or sabclass.
# Private  : Achive by (__) double underscore . Only access in class.

# Public
class employe:
    def __init__(self, name):
        self.name = name  # by default public

    def show(self):
        print(f"Employee Name :{self.name}")

emp1 = employe("amman")
print(emp1.name)
emp1.show()



# Protected 
class employe2:
    def __init__(self, name,salary):
        self.name = name           # Public
        self._salary = salary      # Protectted


    def show(self):
        print(f"Employe Name : {self.name}")
        print(f"Employe Salary : {self._salary}")

emp2 = employe2("abc",25000)
emp2.show()
print(f"Name :{emp2.name}")
print("Salary:" , emp2._salary)

# Private

class student:
    def __init__(self,name,roll,marks):
        self.name = name             # Public
        self._roll = roll            # Protected
        self.__marks = marks         # Private

    def detail(self):
        print(f" Student Name : {self.name}")
        print(f" Student Roll : {self._roll}")

    def show_m(self):
        print(f"Student Marks : {self.__marks}")

class result(student):
    def res(self):
        print(f" Student Name : {self.name}")
        print(f" Student Roll : {self._roll}")
        print(f"Student Marks : {self.__marks}")

s1 = student("abc",102,98)
s1.detail()
s1.show_m()

print("Direct call")
print(s1.name)
print(s1._roll)
# print(s1.__marks) # Show Error
    

r1 = result("abc",302,95)
r1.detail()
r1.show_m()   # Show by method

# r1.res()   # Show Error


# Make the Bank system that protect to update balance 
class Bank:
    def __init__(self,balance):
        self.balance =balance

    def _show(self):
        print(f"Current Balance : {self.balance}")


    def __update(self,amount):
        self.balance+=amount


    def deposite(self,amount):
        if amount > 0:
            self.__update(amount)
            self._show()
        else:
            print("Invalid amount")

# Create object
acc = Bank(5000)
acc._show()
# acc.__update() 

acc.deposite(50000)