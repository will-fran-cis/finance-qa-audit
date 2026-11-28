# Problem 13 (pytest basics: assert, pytest.raises) - easy
#
# money.py has two functions and ONE bug. Write tests that would catch it.
#
# Write one test function per line below. Name each test_<something>, so
# pytest finds it, and give it a name that says what it checks.
#   1. parse_amount("$1,250.50") returns 1250.5
#   2. parse_amount("  42 ") returns 42.0
#   3. parse_amount("") raises ValueError, and the message contains "empty"
#      (use pytest.raises with match=)
#   4. parse_amount("-5") raises ValueError, message contains "negative"
#   5. parse_amount("$1,234,567.89") returns 1234567.89
#   6. apply_interest(1000, 5, 2) returns 1102.5
#
# Run from inside p13_pytest/ with:   python -m pytest test_money.py
# Add -v to see each test's name and result.
#
# Expected: one test fails. Read pytest's failure output from the bottom up:
# which test, which line, and what was the actual error? Then find the bug in
# money.py, fix it, and rerun until all 6 pass.

import pytest

from money import parse_amount, apply_interest

# Your code below
def test_amount_parsing(): 
    assert parse_amount("$1,250.50") == 1250.5
    assert parse_amount("  42 ") == 42.0

    with pytest.raises(ValueError, match="empty"): 
        parse_amount("")

    with pytest.raises(ValueError, match="negative"): 
            parse_amount("-5")

    assert parse_amount("$1,234,567.89") == 1234567.89

def test_apply_interest(): 
     assert apply_interest(1000, 5, 2) == 1102.5