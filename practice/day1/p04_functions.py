# Problem 4 (Tutorial ch. 4: defaults, *args, **kwargs, / and *, lambda, docstrings, annotations) - hard
#
# Part A: the mutable default trap
# Predict the output of the code below BEFORE running it. Then run it.
# Then fix add_question so the second call prints ['q2'].
# Hint: read the "Important warning" in tutorial section 4.9.1.

def add_question(q, bank=None):
    if bank is None: 
        bank = []
    bank.append(q)
    return bank

print(add_question("q1"))
print(add_question("q2"))

# Output: ['q1']
# Output: ['q1','q2']

# Part B
# Write report(name, /, *scores, precision=1, **tags) that RETURNS a string:
#   - name is positional-only, precision is keyword-only (the signature above already does this)
#   - average of scores, formatted to `precision` decimal places
#   - if tags were given, append them as " [k=v, k=v]"
#   - if no scores were given, return f"{name}: no scores" (instead of crashing)
# Add a one-line docstring and type annotations (name: str, scores: float, precision: int,
# tags: str, returns str).
# Hints: f"{x:.{n}f}" formats x to n decimals.  ", ".join(list_of_strings) joins strings.

def report(name: str, /, *scores: float, precision: int = 1, **tags: str) -> str: 
    """Returns string describing model behaviour"""
    tagList=[]
    if scores: 
        avg = f"{(sum(scores) / len(scores)):.{precision}f}"
        if tags: 
            for k, value in tags.items(): 
                tagList.append(f"{k}={value}")
            return f"{name}: avg {avg} over {len(scores)} scores [{", ".join(tagList)}]"
        return f"{name}: avg {avg} over {len(scores)} scores"
    return f"{name}: no scores"


#
# Part C
# Sort results by score, highest first, using sorted() with a lambda key.
results = [("gemini", 4.0), ("groq", 2.5), ("llama", 3.75)]

new_results = sorted(results, key=lambda item: item[1], reverse=True)
print(new_results)
#
# Calls for Part B:
#   print(report("gemini", 4, 5, 3))
#   print(report("groq", 2, 3, precision=2, topic="TFSA", judge="will"))
#   print(report("llama"))
#   print(report.__doc__)
#
# Expected output (after Part A's two lines):
# gemini: avg 4.0 over 3 scores
# groq: avg 2.50 over 2 scores [topic=TFSA, judge=will]
# llama: no scores
# <your docstring>
# [('gemini', 4.0), ('llama', 3.75), ('groq', 2.5)]
#
# Predict, then test each (comment out after):
#   report(name="gemini", scores=4)   -> what error, and which part of the signature causes it?
#   report("gemini", 4, 5, 2)         -> is 2 the precision? Why or why not?

# Your code below

print(report("claude", 4.5, 6.7, 2, 4.5, 6.8, precision=5, user="will", model="opus"))
print(report("gemini", 4, 5, 3))
print(report("groq", 2, 3, precision=2, topic="TFSA", judge="will"))
print(report("llama"))
print(report.__doc__)

print((lambda a, b: a + b)(*(2, 3)))