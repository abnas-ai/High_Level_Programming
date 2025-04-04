
#encapsulation in python

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner #pblic attribute
        self._balance = initial_balance 
        self.__pin = "1234" #private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit must be positive and greater than o")
            
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"withdrawn: {amount}")
            return True
        else:
            print("Withdrawal amount must be positive and less or equal to the balance")
            return False
        
    def get_balance(self):
        return self._balance
    
    def verify_pin(self, attempted_pin):
        return self.__pin == attempted_pin
    
    def change_pin(self, new_pin):
        self.__pin == new_pin
    
    
    
account = BankAccount("Abnas", 2000)
# account.owner = "Mesh"
# print(account.owner) #public attribute
 
# account._balance = 2000
# print(account._balance)#protected attribute

account.change_pin("0000")
print(account.verify_pin("1234"))