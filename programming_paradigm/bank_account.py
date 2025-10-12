class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a certain amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw a certain amount if funds are sufficient."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance formatted to two decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")


