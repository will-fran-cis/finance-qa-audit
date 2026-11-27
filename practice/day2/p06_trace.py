# Problem 6 (Tutorial ch. 8.7: else and finally) - easy, predict-only
#
# This code is already written. Do NOT run it yet.
#
# Step 1. Write your predicted output, line by line, in the block at the bottom.
#         The script ends with a crash: predict the last line of the traceback too.
# Step 2. Run it and compare. For every line you got wrong, write why.
#
# Things to think about:
#   - Which lines run when there is no error? When there is a ValueError?
#   - Does "end" ever print?
#   - Does finally run when the function returns? When it crashes?
#   - tricky(): try returns one thing, finally returns another. Which wins?
#     (8.7 says. Python 3.14 will also print a warning about this; read it.)


def process(text):
    print("start")
    try:
        n = int(text)
        print("converted")
    except ValueError:
        print("bad input")
        return "error"
    else:
        print("no error")
        return n * 2
    finally:
        print("cleanup")
    print("end")


def tricky():
    try:
        return "from try"
    finally:
        "from finally"


print(process("21"))
print("---")
print(process("x"))
print("---")
print(tricky())
print("---")
print(process(None))


#
#
#
# What I got wrong, and why:
#
