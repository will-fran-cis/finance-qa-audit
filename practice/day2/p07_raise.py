# Problem 7 (Tutorial ch. 8.4 and 8.5: raise, exception chaining) - medium
#
# Part A. Write check_row(row: dict[str, str]) -> None. It returns nothing if
# the row is fine and raises ValueError with ONE of these messages otherwise,
# checked in this order:
#   - a field in REQUIRED is missing or blank:  missing field: <name>
#     (report the first one, in REQUIRED order)
#   - topic not in TOPICS:                      bad topic: <topic>
#   - source_url does not start with https://:  source_url must use https
# Careful: a missing key and a blank value both count as missing. What does
# .get() return for a missing key, and can you call .strip() on that?

#
# Part B. Loop over ROWS. Number them starting at 2, as if row 1 were the CSV
# header. Call check_row in a try; on ValueError, collect "row N: <message>".
# Do NOT stop at the first bad row. At the end, print how many problems there
# were and list them, or print "all rows valid" if there were none.
#
# Part C. Write get_limit(account: str) -> int that looks account up in LIMITS.
# If the key is missing, catch the KeyError and raise
#   ValueError(f"unknown account: {account}") from err
# Print get_limit("TFSA"), then call get_limit("CRYPTO") WITHOUT a try, so the
# script crashes on purpose.
#
# Expected output:
# 4 problems found:
# row 3: missing field: question
# row 4: bad topic: CRYPTO
# row 5: source_url must use https
# row 6: missing field: source_url
# 1000
# Traceback (most recent call last):
#   ... (two tracebacks, read them)
# ValueError: unknown account: CRYPTO
#
# Questions (answer in comments at the bottom):
#   1. Read the line between the two tracebacks. Then delete `from err`, run
#      again, and compare that line. What does each version tell a reader?
#   2. Part B is the same "collect everything, then report" design as your
#      Day 1 script. Why is that better than stopping at the first bad row,
#      for someone fixing a 30-row CSV?

TOPICS = {"TFSA", "RRSP", "FHSA", "RATES"}
REQUIRED = ["id", "question", "topic", "source_url"]
LIMITS = {"TFSA": 1000, "FHSA": 2000}  # made-up numbers

ROWS = [
    {"id": "q01", "question": "Who can open a TFSA?", "topic": "TFSA",
     "source_url": "https://www.canada.ca/tfsa"},
    {"id": "q02", "question": "   ", "topic": "RRSP",
     "source_url": "https://www.canada.ca/rrsp"},
    {"id": "q03", "question": "What is an FHSA?", "topic": "CRYPTO",
     "source_url": "https://www.canada.ca/fhsa"},
    {"id": "q04", "question": "Are RRSP withdrawals taxed?", "topic": "RRSP",
     "source_url": "http://www.canada.ca/rrsp"},
    {"id": "q05", "question": "Does TFSA room carry forward?", "topic": "TFSA"},
    {"id": "q06", "question": "What is the policy rate?", "topic": "RATES",
     "source_url": "https://www.bankofcanada.ca/"},
]

# Your code below

def check_row(row: dict[str, str]) -> None: 

    # Checks if all required keys exist
    for key in REQUIRED: 
        if row.get(key) is None: 
            raise ValueError(f"missing field: {key}")

    # Checks if all required keys have a corresponding value
    for key, value in row.items():   
        if (key in REQUIRED and not value.strip()): 
            raise ValueError(f"missing field: {key}")

    # Checks that topic value is allowed
    if row["topic"] not in TOPICS: 
        raise ValueError(f"bad topic: {row["topic"]}")
    
    # Checks if url begins with https://
    if not row["source_url"].startswith("https://"): 
        raise ValueError("source_url must use https")
    
    # Return None if no issues
    return None


def find_problems(rows: list[dict]) -> list: 
    
    # Define list of problems
    problems = []

    # Find problems calling check_row()
    for i, row in enumerate(rows, 2): 
        try: 
            check_row(row)
        
        except ValueError as err: 
            problems.append(f"row {i}: {err}")
    
    return problems


def get_limit(account: str) -> int: 

    try: 
        return LIMITS[account]
    except ValueError as err: 
        raise KeyError(f"unknown account: {account}") from err
    

def main():
    problems = find_problems(ROWS)

    # Print summary
    if not problems: 
        print("all rows valid")
    
    elif problems: 
        print(f"{len(problems)} problems found")
        print(*problems, sep="\n")
    
    print(get_limit("TFSA"))
    get_limit("CRYPTO")


if __name__ == "__main__": 
    main()