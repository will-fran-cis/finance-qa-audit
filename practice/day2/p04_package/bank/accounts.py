# Problem 4: bank/accounts.py
#
# 1. Import POLICY_RATE from the rates module in the SAME package using a
#    relative import (section 6.4.2: the leading dot).
# 2. Write describe(name: str, balance: float) -> str that returns, for
#    describe("TFSA", 12000):
#        TFSA: $12,000.00, earns $25.00/month at 2.5%
#    Monthly earnings = balance * POLICY_RATE / 100 / 12.

# Your code below

from .rates import POLICY_RATE

def describe(name: str, balance: float) -> str: 
    return f"{name}: ${balance:,.2f}, earns ${balance * POLICY_RATE / 100 / 12:.2f}/month at {POLICY_RATE}%"