# Problem 5 (Tutorial ch. 8.3: try/except/else, `as err`) - easy
#
# Write safe_ratio(a: str, b: str) -> str that converts both strings to float
# and divides a by b. It must use try / except / else:
#   - try:    only the risky lines (the two conversions and the division)
#   - except ValueError as err:  return f"bad number ({err})"
#   - except ZeroDivisionError:  return "cannot divide by zero"
#   - else:   return f"{x} / {y} = {result:.2f}"   (x, y are the floats)
#
# Then loop over CASES and print safe_ratio(a, b) for each.
#
# Expected output:
# 10.0 / 4.0 = 2.50
# cannot divide by zero
# bad number (could not convert string to float: 'abc')
# 3.5 / 2.0 = 1.75
# bad number (could not convert string to float: '')
#
# Questions (answer in comments at the bottom):
#   1. Why put the return with the f-string in `else` instead of at the end of
#      the `try` block? (Last paragraph of 8.3's else discussion.)
#   2. What happens if you call safe_ratio(None, "2")? Should this function
#      catch that? Why or why not?
#   3. Where did the text inside the parentheses on line 3 of the output come
#      from? You didn't write it.

CASES = [("10", "4"), ("7", "0"), ("abc", "2"), ("3.5", " 2 "), ("", "1")]

# Your code below

def safe_ratio(a: str, b:str) -> str: 
    try: 
        x = float(a)
        y = float(b)
        result = x / y
    except ValueError as err: 
        return f"bad number ({err})"
    except ZeroDivisionError: 
        return "cannot divide by zero"
    else: 
        return f"{x} / {y} = {result:.2f}"

for x, y in CASES: 
    print(safe_ratio(x, y))