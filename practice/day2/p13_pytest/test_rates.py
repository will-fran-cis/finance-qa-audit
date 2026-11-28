import pytest

from rates import load_rates
# Problem 14 (pytest tmp_path) - medium
#
# Test rates.load_rates. Each test builds its own small CSV inside tmp_path,
# so no test depends on a real file or on another test.
#
# How: a test function that takes a parameter named tmp_path gets a
# pathlib.Path to a fresh empty folder. Make a file path with the / operator
# (path = tmp_path / "rates.csv"), and write text with path.write_text(...).
# load_rates wants a str, so pass str(path). (It would also accept the Path
# directly, since open() takes both. Try it.)
#
# Write these tests:
#   1. A file with a header and 2 good rows loads as a dict with 2 entries,
#      and one date maps to the right rate.

def test_dict_load(tmp_path: str): 

    path = tmp_path / "rates.csv"

    path.write_text(f"{'date'},{'rate'}\n{'2026-10-22'},{'2.2'}\n{'2026-11-12'},{'1.5'}")

    assert len(load_rates(str(path))) == 2
    assert load_rates(str(path))["2026-10-22"] == 2.2

#   2. A file with only the header line raises ValueError, message contains
#      "no rates".
def test_dict_load_2(tmp_path: str): 

    path = tmp_path / "rates.csv"
    
    path.write_text(f"{'date'},{'rate'}")

    with pytest.raises(ValueError, match="no rates"): 
        load_rates(str(path))
                    
#   3. A file whose 2nd data row has the rate "abc" raises ValueError, and the
#      message names the right row number. Work out which number that is
#      before you write the match= (look at enumerate(..., start=2)).
def test_dict_load_3(tmp_path: str): 

    path = tmp_path / "rates.csv"

    path.write_text(f"{'date'},{'rate'}\n{'2026-10-22'},{'2.2'}\n{'2026-11-12'},{'abc'}")

    with pytest.raises(ValueError, match="3"): 
        load_rates(str(path))
    

#   4. A path that doesn't exist raises FileNotFoundError. (Which exception
#      does open() raise? You don't need to write any file for this one.)

def test_dict_load_4(tmp_path: str): 

    with pytest.raises(FileNotFoundError): 
        load_rates("file_doesn't_exist")


# Sample file content (\n is a newline inside a Python string):
#   "date,rate\n2026-10-29,2.25\n2026-10-30,2.25\n"
#
# Run from inside p13_pytest/:   python -m pytest -v
# (With no file name, pytest runs every test_*.py file here, so you'll see
# problem 13's tests too.)
#
# Expected: all 4 pass. Then break one on purpose (for example, change the
# expected row number) to see what a failing match= looks like.

# Your code below
