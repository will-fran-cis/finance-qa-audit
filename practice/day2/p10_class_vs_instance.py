# Problem 10 (Tutorial ch. 9.3.5: class vs instance variables) - easy
#
# This code is already written, and has a bug.
#
# Step 1. Do NOT run it yet. Predict all five output lines and write them in
#         the block at the bottom.
# Step 2. Run it. If you were wrong, work out why (compare the `tricks`
#         example in 9.3.5).
# Step 3. Fix the class so each Portfolio has its own holdings, while `count`
#         still counts every Portfolio ever made. Change only the class.
#
# Expected output after the fix:
# Ana ['XIC']
# Ben ['VFV']
# 2 2 2
# 0
# 2
#
# The last two lines: `p1.count = 0` is already in the code below. Why does it
# change p1.count but not Portfolio.count? What did that line actually create?


class Portfolio:
    count = 0

    def __init__(self, owner):
        self.owner = owner
        Portfolio.count += 1
        self.holdings = []

    def add(self, ticker):
        self.holdings.append(ticker)


p1 = Portfolio("Ana")
p2 = Portfolio("Ben")
p1.add("XIC")
p2.add("VFV")
print(p1.owner, p1.holdings)
print(p2.owner, p2.holdings)
print(p1.count, p2.count, Portfolio.count)
p1.count = 0
print(p1.count)
print(Portfolio.count)

# My prediction (before the fix):
#
# 
