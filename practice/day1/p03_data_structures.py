# Problem 3 (Tutorial ch. 5: comprehensions, sets, dicts, looping techniques) - medium/hard
#
# Each row is (id, topic, difficulty).
rows = [
    ("q1", "TFSA", "easy"),
    ("q2", "RRSP", "hard"),
    ("q3", "TFSA", "medium"),
    ("q4", "FHSA", "easy"),
    ("q5", "RATES", "hard"),
    ("q6", "TFSA", "easy"),
    ("q2", "RRSP", "medium"),
]
#
# 1. One list comprehension: the ids of all "easy" rows.
# 2. A set of the unique topics. Print it as a sorted list.
# 3. Find duplicate ids with a loop and a set named `seen`. Print them as a list.
# 4. Count rows per topic into a dict, using .get() (no if/else).
#    Print one line per topic, sorted by topic name, with .items() and an f-string.
# 5. (hard) One dict comprehension mapping each topic -> list of its ids, in row order.
#    Keys sorted. Hint: a comprehension inside a comprehension.

l = [row[0] for row in rows if row[-1] == "easy"]
print(l)

topics = set()
for row in rows: 
    topics.add(row[1])
sort = sorted(list(topics))
print(sort)

seen = set()
listed = []
for row in rows: 
    if row[0] in seen: 
        listed.append(row[0])
    seen.add(row[0])
print(listed)

d = {}
for row in rows: 
    d[row[1]] = d.get(row[1], 0) + 1
for topic, num in sorted(d.items()): 
    print(f"{topic}: {num}")

print({topic: [row[0] for row in rows if row[1] == topic] for topic in sorted(topics)})

d2 = {}
for topic in sorted(topics): 
    d2[topic] = []
    for qid, t, _ in rows: 
        if topic == t: 
            d2[topic].append(qid)
#
# Expected output:
# ['q1', 'q4', 'q6']
# ['FHSA', 'RATES', 'RRSP', 'TFSA']
# ['q2']
# FHSA: 1
# RATES: 1
# RRSP: 2
# TFSA: 3
# {'FHSA': ['q4'], 'RATES': ['q5'], 'RRSP': ['q2', 'q2'], 'TFSA': ['q1', 'q3', 'q6']}
#
# Predict first: is type({}) a dict or a set? How do you make an empty set?

# Your code below
