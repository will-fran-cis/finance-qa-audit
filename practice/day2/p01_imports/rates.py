# Problem 1, part 1 of 2 (Tutorial ch. 6.1: import styles) - easy
#
# This file is a module. It only DEFINES things; it does no work at the top level.

# Write:
#   1. A constant POLICY_RATE set to 2.5 (a made-up number, a percent).
#   2. A function monthly_interest(balance: float, annual_rate: float) -> float
#      that returns balance * annual_rate / 100 / 12, rounded to 2 decimals.
#
# Then go to main.py.

# Your code below
POLICY_RATE = 2.5

def monthly_interest(balance: float, annual_rate: float) -> float: 
    return round(balance * annual_rate / 100 / 12, 2)