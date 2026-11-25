import csv
import json

# File paths (relative, so run from the repo root)
DATA_PATH = "data/questions.csv"
JSON_PATH = "data/clean_questions.json"

# Allowed values used by the validation checks
ALLOWED_TOPICS = {"TFSA", "RRSP", "FHSA", "RATES"}
ALLOWED_DIFFICULTIES = {"easy", "medium", "hard"}
ALLOWED_URL_BEGINNING = "https://"

# Load every row of the CSV as a dict keyed by the header names
with open(DATA_PATH, "r", encoding="utf-8") as data:
    reader = csv.DictReader(data)
    data_list = list(reader)

# Validation state
errors = []
unique_id_list = set()

# Rows sorted by whether they passed every check
clean_rows = []
dirty_rows = []

# Counts per topic and per difficulty
seen_topic_dict = dict()
seen_difficulty_dict = dict()

# Validate each row; start=2 so i matches the file's line number (line 1 is the header)
for i, row in enumerate(data_list, start=2):

    # Error count before this row, used later to tell if this row added any
    temp_errors = len(errors)

    # Required fields: no value may be empty or whitespace only
    for key, value in row.items():
        if not value.strip():
            errors.append(f"Row {i} has missing info")

    # Unique ids
    if row["id"] in unique_id_list:
        errors.append(f"ID {row["id"]} appears multiple times (row {i}).")
    unique_id_list.add(f"{row["id"]}")

    # Topic must be one of the allowed topics
    if row["topic"] not in ALLOWED_TOPICS:
        errors.append(f"Problem with ID {row["id"]}, row {i}, has topic: {row["topic"]!r}")

    # Difficulty must be one of the allowed levels
    if row["difficulty"] not in ALLOWED_DIFFICULTIES:
        errors.append(f"Problem with ID {row["id"]} row {i}, has difficulty: {row["difficulty"]!r}")

    # Source URL must use https
    if not row["source_url"].startswith(ALLOWED_URL_BEGINNING):
        errors.append(f"Problem with ID {row["id"]} row {i}, has url: {row["source_url"]!r}")

    # Tally topic and difficulty (counts every row, valid or not)
    seen_topic_dict[row["topic"]] = seen_topic_dict.get(row["topic"], 0) + 1
    seen_difficulty_dict[row["difficulty"]] = seen_difficulty_dict.get(row["difficulty"], 0) + 1

    # No new errors for this row means it is clean
    clean_rows.append(row) if len(errors) == temp_errors else dirty_rows.append(row)

# Export the valid rows to JSON
with open(JSON_PATH, "w", encoding="utf-8") as json_file:
    json.dump(clean_rows, json_file, indent=2, ensure_ascii=False)

# Summary
print(f"Errors: {errors}")
print(f"Topics: {seen_topic_dict}")
print(f"Difficulties: {seen_difficulty_dict}")


# Checkpoint: export only the questions for one topic

def newJson(topic: str, path: str) -> None:
    """Take topics with a given name and write them to a new JSON file"""
    topic_qs = []
    for i, row in enumerate(data_list):
        if row["topic"] == topic:
            topic_qs.append(row)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(topic_qs, f, indent=2, ensure_ascii=False)


newJson("FHSA", "assignments/checkpoint_fhsa.json")
