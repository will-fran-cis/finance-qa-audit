# Problem 11 (Tutorial ch. 9.5: inheritance, super(), isinstance) - medium
#
# Start with: from p09_class_basics import Account
# Run this file. If p09's demo output appears too, go back to ch. 6:
# what is missing from p09?
from p09_class_basics import Account
#
# Part A. Write class TFSA(Account). A TFSA has contribution room.
#   __init__(self, owner: str, balance: float, room: float)
#       call the parent's __init__ with super(), with kind "TFSA",
#       then store room.
#   deposit(self, amount: float) -> None        (overrides Account.deposit)
#       if amount > self.room: raise ValueError(f"over room by ${amount - self.room:,.2f}")
#       otherwise let the PARENT's deposit do the balance update (super()),
#       then reduce room by amount.
#   describe(self) -> str                       (overrides Account.describe)
#       the parent's describe() text plus f" (room left: ${self.room:,.2f})"
#       Reuse the parent's method with super(); do not rebuild the string.
#   withdraw is NOT written here: TFSA inherits it unchanged.

class TFSA(Account): 

    def __init__(self, owner: str, balance: float, room: float): 
        super().__init__(owner=owner, kind="TFSA", balance=balance)
        self.room = room
        
    def deposit(self, amount: float) -> None: 
        if amount > self.room: 
            raise ValueError(f"over room by ${amount - self.room:,.2f}")
        super().deposit(amount)
        self.room -= amount
    
    def describe(self) -> str: 
        return super().describe() + " " + f"(room left: ${self.room:,.2f})"


# Part B. In main() under a guard:
#   t = TFSA("Ana", 1000, 2000)          (made-up numbers)
#   t.deposit(500);  print(t.describe())
#   try t.deposit(2000); on ValueError print f"error: {err}"
#   try t.deposit(-5);   on ValueError print f"error: {err}"
#   t.withdraw(300);  print(t.describe())
#   print isinstance(t, TFSA), isinstance(t, Account),
#         isinstance(Account("Ben", "RRSP"), TFSA)  on one line
#   print issubclass(TFSA, Account)
# Expected output:
# Ana's TFSA: $1,500.00 (room left: $1,500.00)
# error: over room by $500.00
# error: amount must be positive
# Ana's TFSA: $1,200.00 (room left: $1,500.00)
# True True False
# True
#
# Think about:
#   - The -5 deposit: whose error message is that, and why did your TFSA
#     room check not catch it?
#   - In deposit, why reduce room AFTER super().deposit(), not before?
#     What would happen to room on the -5 deposit if you did it before?

def main(): 
    new_account = TFSA("Ana", 1000, 2000)
    print(new_account.describe())
    print(new_account.owner, new_account.balance, new_account.kind, new_account.room)

# Your code below
if __name__ == "__main__": 
    main()