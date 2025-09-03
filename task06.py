class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("pulingiz kam")

    def get_balance(self):
        return self.__balance
    

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())