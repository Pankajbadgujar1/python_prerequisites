class BankAccount:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited , New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")

        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}" )

account = BankAccount("Pankaj",5000)
print(account.balance)

account.withdraw(500)
print(account.balance)

account.deposit(2000)


""" 
Object oriented programming allows you to model real -world scenarios using classes and objects.


"""