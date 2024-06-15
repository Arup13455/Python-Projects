'''class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def credit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} was credited from {self.acc_no}.")
        print(f"Total balance: {self.get_balance()}")
    
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs.{amount} was debited from {self.acc_no}.")
        print(f"Total balance: {self.get_balance()}")
    
    def get_balance(self):
        return self.balance
    

a = int(input("enter your balance: "))
b = int(input("enter your account no.: "))
acc1 = Account(a, b)
choice = input("what do you want (Credit?Debit): ")
if  choice.lower() == "credit":
    money = int(input("How much money do you want to credit: "))
    acc1.credit(money)
elif choice.lower() == "debit":
    money = int(input("How much money do you want to debit: "))
    acc1.debit(money)
else:
    print("Invalid Input!")'''
# A python program to create a Bank class where deposits and withdrawals can be handled by using instance methods
import sys
class Bank:
    """Bank related transactions"""
    def __init__(self, name, balance, acc_no):
        self.name = name
        self.balance = balance
        self.acc_no = acc_no
    # to add deposit amount to balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    # to deduct withdrawal amount from the balance
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawals can't be possible because of low balance.")
        else:
            self.balance -= amount
            return self.balance
name = input("Enter your name: ")
balance = float(input("Enter your balance: "))
acc_no = int(input("Enter your account no. : "))

user1 = Bank(name, balance, acc_no)
while(True):
    print("d- Deposit, w - Withdraw, e - Exit.")
    choice = input("Enter your choice: ")
    if choice.lower() == "e":
        sys.exit()
    elif choice.lower() == "w":
        amount = float(input("Enter the amount you want to withdraw: "))
        print(f"Balance after withdrawal from {user1.acc_no}: {user1.withdrawal(amount)}")
    else:
        amount = float(input("Enter the amount you want to deposit: "))
        print(f"Balance after deposit from {user1.acc_no}: {user1.deposit(amount)}")

