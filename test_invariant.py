import invariant_python

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def __invariant__(self):
        print("Checking invariants...")
        if self.balance < 0:
            raise ValueError("Invariant failed: Balance cannot be negative.")

# Create an account with 100 balance
account = BankAccount(100)

# Call withdraw(50) using wrap_method_call
print("Withdrawing 50...")
invariant_python.wrap_method_call(account, account.withdraw, (50,))

# Call withdraw(100) which should violate the invariant
print("Withdrawing 100...")
invariant_python.wrap_method_call(account, account.withdraw, (100,))
