import json
# Problem 5 (Tutorial ch. 7: f-string formatting, files, json) + type annotations - medium/hard
#
# Run this from the repo root so the relative paths below work:
#   python3 practice/day1/p05_files_json.py
#
# Every function must have a docstring and full type annotations (parameters and return).
#
results = [("gemini", 4.0), ("groq", 2.5), ("llama", 3.75)]
TXT_PATH = "practice/day1/results.txt"
JSON_PATH = "practice/day1/results.json"
#
# Part A
# write_table(rows, path) writes a fixed-width text table. rows is a list of (str, float) tuples.
#   - Use `with` and encoding="utf-8".
#   - Name left-aligned in 10 characters, score right-aligned in 6 with 2 decimals.
#   - Returns nothing.
# Hint: format specs like {x:<10} and {x:>6.2f}. Tutorial 7.1.1.

def write_table(rows: list[tuple[str, float]], path: str) -> None:
    """Write data in table form to a file"""
    with open(path, "w", encoding="utf-8") as f: 
        f.write(f"{'model':<10}{'score':>6}\n")
        for model, num in rows: 
            f.write(f"{model:10}{num:>6.2f}\n")

write_table(results, TXT_PATH)
#
# Expected contents of results.txt:
# model      score
# gemini      4.00
# groq        2.50
# llama       3.75
#
# Part B
# read_table(path) reads results.txt back and returns a list of (str, float) tuples.
#   - Skip the header line.
#   - Loop over the file object directly (tutorial 7.2.1), use .split(), convert the score.

def read_table(path: str) -> list[tuple[str, float]]: 
    """Read a table in an external file and return it"""
    with open(path, "r", encoding="utf-8") as f: 
        f.readline()
        lis = []
        for line in f: 
            model, score = line.split()
            lis.append((model, float(score)))
        return lis

print(read_table(TXT_PATH))

# Part C
# save_json(scores, path) writes a dict like {"gemini": 4.0, ...} with indent=2.
# load_json(path) reads it back and returns the dict.
# Hint: dict(results) turns a list of pairs into a dict.

def save_json(scores: dict[str, float], path: str) -> None:
    """Save the dictionary into a file in json format"""
    with open(path, "w", encoding="utf-8") as f: 
        json.dump(scores, f, indent=2)

save_json(dict(results), JSON_PATH)

def load_json(path: str) -> dict[str, float]: 
    """Read json into the terminal"""
    with open(path, "r", encoding="utf-8") as f: 
        return json.load(f)

print(load_json(JSON_PATH))

#
# Part D
# total = the sum of all scores. Print it with the = specifier, then print a name with !r.
total = sum(scores for model, scores in results)
print(f"{total=}")
print(f"{results[0][0]!r} vs {results[0][0]}")

#
# Expected terminal output:
# [('gemini', 4.0), ('groq', 2.5), ('llama', 3.75)]
# {'gemini': 4.0, 'groq': 2.5, 'llama': 3.75}
# True
# total=10.25
# 'groq' vs groq
#
# (Line 3 is: is the loaded JSON dict == dict(results)?)
#
# Final check: add write_table("oops", 5) at the bottom and look at it in VS Code.
# If nothing is underlined, set "python.analysis.typeCheckingMode" to "basic" in VS Code settings.
# Read the message Pylance shows, then delete the line.

# Your code below
