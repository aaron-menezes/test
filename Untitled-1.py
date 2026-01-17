class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive")
    
    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

# Example usage
if __name__ == "__main__":
    account = BankAccount("John", 1000)
    account.check_balance()
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()