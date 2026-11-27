# Problem 9 (Tutorial ch. 9.3: class, __init__, self, methods) - easy
#
# Part A. Write a class Account.
#   __init__(self, owner: str, kind: str, balance: float = 0.0)
#       stores all three as instance attributes.
#   deposit(self, amount: float) -> None
#       raises ValueError("amount must be positive") if amount <= 0,
#       otherwise adds amount to the balance.
#   withdraw(self, amount: float) -> None
#       raises ValueError if amount > balance, with the message
#       f"insufficient funds: balance ${self.balance:,.2f}, tried ${amount:,.2f}"
#       otherwise subtracts it.
#   describe(self) -> str
#       returns e.g. "Ana's TFSA: $1,250.00"
class Account: 

    def __init__(self, owner: str, kind: str, balance: float = 0.0): 
        self.owner = owner
        self.kind = kind
        self.balance = balance
    
    def deposit(self, amount: float) -> None: 
        if amount <= 0: 
            raise ValueError("amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance: 
            raise ValueError(f"insufficient funds: balance ${self.balance:,.2f}, tried ${amount:,.2f}")
        if amount <= 0: 
            raise ValueError("amount must be positive")
        self.balance -= amount

    def describe(self) -> str: 
        return f"{self.owner}'s {self.kind}: ${self.balance:,.2f}"


# Part B. Put this demo in a main() function, called under an
# if __name__ == "__main__": guard (p11 will import Account from this file):
#   - a = Account("Ana", "TFSA");  b = Account("Ben", "RRSP", 500)
#   - a.deposit(1250);  b.withdraw(200)
#   - print a.describe(), then b.describe()
#   - print Account.describe(b)      <- predict this one first
#   - try a.withdraw(5000); on ValueError print f"error: {err}"
#   - print(a)                       <- see what Python shows

def main(): 
    x = Account("Will", "TFSA", 1000)
    print(x.describe())
    x.deposit(1000)
    print(x.describe())
    x.withdraw(500)
    print(x.describe())

if __name__ == "__main__": 
    main()
# Expected output (the last line's hex number will differ):
# Ana's TFSA: $1,250.00
# Ben's RRSP: $300.00
# Ben's RRSP: $300.00
# error: insufficient funds: balance $1,250.00, tried $5,000.00
# <__main__.Account object at 0x7f...>
#
# Think about: Account.describe(b) and b.describe() give the same result.
# What does that tell you about where `self` comes from? (9.3.4)
# And print(a) is not very useful. Remember it when you meet dataclasses.

# Your code below
