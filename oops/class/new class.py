#Crated a simple student result portal using 'class'

class student:
    def __init__(self,name,marks,grade):
        self.name = name
        self.marks = marks
        self.grade = grade

    def greet(self):
        print("welcome to the result portal,",self.name)

    def display(self):
        print("Name:", self.name)
        print("Marks:",self.marks)
        print("Grade:", self.grade)

s1 = student ("samyuktha", 92,"A+")
s1.greet()
s1.display()


#Bank Account example

class BankAcc:
    def __init__ (self,holder, balance):
        self.holder= holder
        self.balance = balance

    def deposit (self,amount):
        self.balance = self.balance+amount
        print("deposit:",amount)

    def withdrawal (self, amount):
        if amount > self.balance:
            print("Insuffient balance!")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:",amount)

    def display(self):
       print("Holder:", self.holder)
       print("balance", self.balance)


b1 = BankAcc ("sam",2000)

b1.deposit(0)
b1.withdrawal(200)
b1.display()






























