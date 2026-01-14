# Banking System 

class Bank:
    def __init__ (self,name ,acc_num,branch,pin):
        self.name = name
        self.acc_num = acc_num
        self.branch = branch
        self.balance = 1000
        self. pin = pin

    def info(self):
        print(f"Account Owner is {self.name}")
        print(f"Account Number is :{self.acc_num}")
        print(f"Account Branch is {self.branch}")

    def credit(self,amount):
        self.balance += amount
        n_b = print("Update balance is ",self.balance)
        return n_b
    
    def debit(self , amount):
        p = int(input("Enter your pin : "))
        if p == self.pin:
            if amount > self.balance:
                print(f"The balance is less than {amount}. So you cant withdrow")
            else:
                self.balance -= amount
                print("Update balance is ",self.balance)
        else:
            return "Wrong Pin"
    
    def bal(self):
        p = int(input("Enter your pin :"))
        if p == self.pin:
            print("Current balance :",self.balance)
        else:
            print("Update balance is ",self.balance)


# Creating first account
# acc1 = Bank("abc",114477,"jaipur",2230)

# acc1.info()  # Call the info method

# acc1.credit(10000) # call credit method

# acc1.debit(5000) # call debit method 

# acc1.credit(7000)

# acc1.bal()  # call balance method


# Creating second account
acc2 = Bank("xyz",442233,"dehli",1123)

acc2.info()  # Call the info method

acc2.credit(10000) # call credit method

acc2.debit(4500) # call debit method 

acc2.credit(6500)

acc2.bal()  # call balance method