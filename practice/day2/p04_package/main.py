# Problem 4: main.py (sits NEXT TO the bank/ folder, not inside it)
#
# Use three different import styles:
#   A. `import bank.accounts`  then print bank.accounts.describe("TFSA", 12000)
#   B. `from bank import rates`  then print rates.POLICY_RATE
#   C. `from bank.accounts import describe`  then print describe("RRSP", 4800)
#
import bank.accounts
print(bank.accounts.describe("TFSA", 12000))

from bank import rates
print(rates.POLICY_RATE)

from bank.accounts import describe
print(describe("RRSP", 4800))
# Predict before running: how many times does "bank package imported" print?
#
# Run from inside p04_package/:  python3 main.py
#
# Expected output:
# bank package imported
# TFSA: $12,000.00, earns $25.00/month at 2.5%
# 2.5
# RRSP: $4,800.00, earns $10.00/month at 2.5%
#
# Then run these two from inside p04_package/ and explain the difference in a
# comment below. This is why you'll use `python -m finance_qa.cli` today.
#   python3 bank/accounts.py      (read the error message carefully)
#   python3 -m bank.accounts
# Hint for the explanation: when accounts.py runs as a plain script, what is
# its __name__, and does Python know it belongs to the bank package?

# Your code below
