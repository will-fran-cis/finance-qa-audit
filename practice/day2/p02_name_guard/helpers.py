# Problem 2 (Tutorial ch. 6.1.1: __name__ and import caching) - easy
#
# This file is already written. It has a problem: it runs a "quick test"
# at the top level.
#
# Step 1. Do NOT run anything yet. Read helpers.py and report.py, then write
#         your prediction of `python3 report.py`'s output in the comment
#         block at the bottom of report.py. Think about:
#           - which lines in helpers.py run when it is imported
#           - what happens the SECOND time report.py imports helpers
# Step 2. Run `python3 report.py` and compare with your prediction.
# Step 3. Fix THIS file so that:
#           `python3 report.py`  prints only the report lines
#           `python3 helpers.py` still runs the quick test
#         Do not delete the test code; move it.
#
# Expected output after the fix:
#
# $ python3 report.py
# Report
# $99.00
# $5.00
#
# $ python3 helpers.py
# Testing format_money...
# $1,234.50


def format_money(amount: float) -> str:
    return f"${amount:,.2f}"

if __name__ == "__main__": 
    print("Testing format_money...")
    print(format_money(1234.5))
