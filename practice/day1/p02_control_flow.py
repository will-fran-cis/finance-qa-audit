# Problem 2 (Tutorial ch. 4: for, enumerate, break, for/else, match, functions) - medium
#
# Part A
# Write check_deposits(deposits, limit=7000). deposits is a list of (date, amount) tuples.
# - Loop with enumerate, numbering from 1.
# - Keep a running total. If adding a deposit pushes the total over the limit,
#   print the over-contribution line and stop the loop.
# - Otherwise print the deposit line.
# - Use the loop's else clause (not a flag variable) to print the "no over-contribution" line.

def check_deposits(deposits, limit=7000): 
    total = 0
    for counter, (date, amount) in enumerate(deposits, start=1): 
        total += amount
        if total > limit:
            print(f"Over-contribution on {date} by {total - limit}")
            break
        print(f"{counter}. {date}: +{amount} (total {total})")
    else: 
        print(f"No over-contribution. Room left: {limit - total}")


#
# Part B
# Write describe(account) using a match statement:
#   "RRSP" or "FHSA" -> "deductible contributions"   (one case, use |)
#   "TFSA"           -> "tax-free growth"
#   anything else    -> f"unknown account: {account}"

def describe(account): 
    match account: 
        case "RRSP" | "FHSA":
            return "deductible contributions"
        case "TFSA": 
            return "tax-free growth"
        case _: 
            return f"unknown account: {account}"
#
# Test data:
deposits_a = [("2024-01-15", 2000), ("2024-03-02", 1500), ("2024-06-30", 3000), ("2024-09-10", 1000)]
deposits_b = [("2024-02-01", 3000), ("2024-05-01", 2500)]
#
# Call check_deposits on both lists, then describe() on "TFSA", "FHSA", "RESP".
#
# Expected output:
# 1. 2024-01-15: +2000 (total 2000)
# 2. 2024-03-02: +1500 (total 3500)
# 3. 2024-06-30: +3000 (total 6500)
# Over-contribution on 2024-09-10 by 500
# 1. 2024-02-01: +3000 (total 3000)
# 2. 2024-05-01: +2500 (total 5500)
# No over-contribution. Room left: 1500
# tax-free growth
# deductible contributions
# unknown account: RESP
#
# Predict first: when does a for loop's else clause run, and when doesn't it?

# Your code below
check_deposits(deposits_a)
check_deposits(deposits_b)

print(describe("RRSP"))
print(describe("FHSA"))
print(describe("TFSA"))
print(describe("RESP"))