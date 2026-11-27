ATTEMPTS = [(5000, 1200), (5000, -50), (1000, 1500), (300, 300)]

# Problem 8 (Tutorial ch. 8.6: user-defined exceptions) - medium
#
# You haven't read ch. 9 (classes) yet. For now this is all you need:
#     class MyError(Exception):
#         pass
# makes a new exception type that behaves like Exception. Putting a different
# class in the parentheses makes it a "child" of that class.
#
# Part A. Define three exception types:
#   - ContributionError, a child of Exception (the base for this "package")
#   - OverContributionError, a child of ContributionError
#   - NegativeAmountError, a child of ContributionError
class ContributionError(Exception): 
    pass

class OverContributionError(ContributionError): 
    pass

class NegativeAmountError(ContributionError): 
    pass
#
# Part B. Write contribute(room: float, amount: float) -> float that returns
# the room left after contributing. Raise:
#   - NegativeAmountError(f"amount must be positive, got {amount}") if amount <= 0
#   - OverContributionError(f"over by ${amount - room:,.2f}")       if amount > room

def contribute(room: float, amount: float) -> float: 
    
    if amount <= 0: 
        raise NegativeAmountError(f"amount must be positive, got {amount}")

    if amount > room: 
        raise OverContributionError(f"over by ${amount - room:,.2f}")

    return room - amount

# Part C. Loop over ATTEMPTS. For each (room, amount), call contribute with
# exactly these handlers, in this order:
#   - except OverContributionError as err:  print(f"over-contribution: {err}")
#   - except ContributionError as err:      print(f"rejected: {err}")
#   - else:                                 print(f"ok, room left: ${new_room:,.2f}")

for room, amount in ATTEMPTS: 
    
    try: 
        new_room = contribute(room, amount)
    
    except OverContributionError as err: 
        print(f"over-contribution: {err}")
    
    except ContributionError as err: 
        print(f"rejected: {err}")
    
    else: 
        print(f"ok, room left: ${new_room:,.2f}")

# Expected output:
# ok, room left: $3,800.00
# rejected: amount must be positive, got -50
# over-contribution: over by $500.00
# ok, room left: $0.00
#
# Questions (answer in comments at the bottom):
#   1. There is no `except NegativeAmountError`. Why was it still caught?
#   2. Swap the two except clauses and run again. What changes, and why?
#      (Compare the B, C, D example in 8.3.)
#   3. Why make your own base class instead of raising ValueError for
#      everything? Think about cli.py: it wants to catch "any problem with the
#      user's data" but not real bugs in your code.


# Your code below
