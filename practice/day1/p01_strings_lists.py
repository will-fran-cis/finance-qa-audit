# Problem 1 (Tutorial ch. 3: numbers, strings, lists) - easy
#
# Given:
account = "TFSA-2024-0042"
balances = [1200, 3400, 560, 7800, 90]
#
# Print, one per line, using only indexing, slicing, len(), and arithmetic:
#   1. The account type (the first 4 characters)
#   2. The last 4 characters
#   3. The number of balances
#   4. The total of the first and last balance
#   5. The balances list reversed (use a slice, not .reverse())
#   6. The average balance as a float, then the same average with // (floor division)
#
# Then replace the middle three balances with [0, 0] in ONE slice assignment
# and print the list.
#
# Expected output:
# TFSA
# 0042
# 5
# 1290
# [90, 7800, 560, 3400, 1200]
# 2610.0
# 2610
# [1200, 0, 0, 90]
#
# Predict first: what does account[20] do? What about account[10:20]? Try both.

# Your code below

print(account[:4])
print(account[-4:])
print(len(balances))
print(balances[0] + balances[-1])
print(balances[::-1])

total = 0
for balance in balances: 
    total += balance
print(total / len(balances))

print(total // len(balances))
balances[1:4] = [0, 0]
print(balances)

