# Problem 3 (Tutorial ch. 6.1.1: sys.argv, scripts) - medium
#
# Write a script that takes a TOPIC and a LIMIT on the command line and prints
# up to LIMIT matching questions as "id: question".
#
# Rules:
#   - All logic goes in a function main() -> None, called under an
#     if __name__ == "__main__": guard.
#   - Topic matching ignores case (rrsp matches RRSP).
#   - Wrong number of arguments: print  usage: p03_argv.py TOPIC LIMIT
#     and stop with sys.exit(1).
#   - LIMIT that is not a whole number: print  error: LIMIT must be a whole number
#     and stop with sys.exit(1). You haven't read about exceptions yet, so check
#     with str.isdigit() instead of try/except.
#   - No matches: print  No questions for topic CRYPTO  (using the topic as typed).
#
# Expected output (run from practice/day2/):
#
# $ python3 p03_argv.py TFSA 2
# q01: Who can open a TFSA?
# q02: Do TFSA withdrawals count as taxable income?
#
# $ python3 p03_argv.py rrsp 5
# q03: What is the deadline to contribute to an RRSP for a tax year?
# q06: What happens to an RRSP at age 71?
#
# $ python3 p03_argv.py
# usage: p03_argv.py TOPIC LIMIT
#
# $ python3 p03_argv.py TFSA two
# error: LIMIT must be a whole number
#
# $ python3 p03_argv.py CRYPTO 3
# No questions for topic CRYPTO
#
# Extra: right after a run, `echo $?` prints the exit status of the last
# command. Compare it after a good run and after a usage error. What is the
# exit status for, and who reads it?

import sys

QUESTIONS = [
    {"id": "q01", "topic": "TFSA", "question": "Who can open a TFSA?"},
    {"id": "q02", "topic": "TFSA", "question": "Do TFSA withdrawals count as taxable income?"},
    {"id": "q03", "topic": "RRSP", "question": "What is the deadline to contribute to an RRSP for a tax year?"},
    {"id": "q04", "topic": "FHSA", "question": "How long can an FHSA stay open?"},
    {"id": "q05", "topic": "TFSA", "question": "Does unused TFSA room carry forward?"},
    {"id": "q06", "topic": "RRSP", "question": "What happens to an RRSP at age 71?"},
]

def main() -> None: 

    if len(sys.argv) != 3: 
        print("usage: p03_argv.py TOPIC LIMIT")
        sys.exit(1)

    if not sys.argv[2].isdigit(): 
        print("error: LIMIT must be a whole number")
        sys.exit(1)

    TOPIC = sys.argv[1].lower()
    LIMIT = int(sys.argv[2])

    output = 0

    for row in QUESTIONS: 
        if output >= LIMIT: 
            break
        if row["topic"].lower() == TOPIC: 
            output += 1
            print(f"{row["id"]}: {row["question"]}")
    
    if not output: 
        print(f"No questions for topic {TOPIC.upper()}")
        

# Your code below
if __name__ == "__main__": 
    main()