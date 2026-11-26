# Problem 1, part 2 of 2 (Tutorial ch. 6.1: import styles) - easy
#
# Use rates.py from this file, importing it three different ways.
#
#   A. `import rates`. Print rates.POLICY_RATE, then
#      rates.monthly_interest(12000, rates.POLICY_RATE).
#   B. `from rates import monthly_interest`. Call monthly_interest(12000, 2.5)
#      with no "rates." prefix and print it.
#   C. `import rates as r`. Print r.monthly_interest(12000, r.POLICY_RATE).
#   D. Print rates.__name__, then print __name__ on its own.
#
# Run it with: python3 main.py   (from inside p01_imports/)
#
# Expected output:
# 2.5
# 25.0
# 25.0
# 25.0
# rates
# __main__
#
# Questions (answer in comments at the bottom, then test in the REPL):
#   1. In a brand new REPL, run only `from rates import monthly_interest`.
#      Does `rates.POLICY_RATE` work? Why or why not?
#   2. Why does D print two different names?
#   3. After running main.py, a __pycache__/ folder appears. What is it?
#      (Section 6.1.3.) Should it be committed to git?

# Your code below

import rates
from rates import monthly_interest
import rates as r

print(rates.POLICY_RATE)
print(rates.monthly_interest(12000, rates.POLICY_RATE))

print(monthly_interest(12000, 2.5))

print(r.monthly_interest(12000, r.POLICY_RATE))

print(rates.__name__)
print(__name__)

