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
