import csv
import json

DATA_PATH = "data/questions.csv"
JSON_PATH = "data/clean_questions.json"
ALLOWED_TOPICS = {"TFSA", "RRSP", "FHSA", "RATES"}
ALLOWED_DIFFICULTIES = {"easy", "medium", "hard"}
ALLOWED_URL_BEGINNING = "https://"

with open(DATA_PATH, "r", encoding = "utf-8") as data: 
    reader = csv.DictReader(data)
    data_list = list(reader)

errors = []
unique_id_list = set()

clean_rows = []
dirty_rows = []

seen_topic_dict = dict()
seen_difficulty_dict = dict()

for i, row in enumerate(data_list, start=2): 

    temp_errors = len(errors)

    for key, value in row.items(): 
        if not value.strip(): 
            errors.append(f"Row {i} has missing info")

    if row["id"] in unique_id_list: 
        errors.append(f"ID {row["id"]} appears multiple times (row {i}).")
    unique_id_list.add(f"{row["id"]}")

    if row["topic"] not in ALLOWED_TOPICS: 
        errors.append(f"Problem with ID {row["id"]}, row {i}, has topic: {row["topic"]!r}")
    
    if row["difficulty"] not in ALLOWED_DIFFICULTIES: 
        errors.append(f"Problem with ID {row["id"]} row {i}, has difficulty: {row["difficulty"]!r}")
    
    if not row["source_url"].startswith(ALLOWED_URL_BEGINNING): 
        errors.append(f"Problem with ID {row["id"]} row {i}, has url: {row["source_url"]!r}")

    seen_topic_dict[row["topic"]] = seen_topic_dict.get(row["topic"], 0) + 1
    seen_difficulty_dict[row["difficulty"]] = seen_difficulty_dict.get(row["difficulty"], 0) + 1

    clean_rows.append(row) if len(errors) == temp_errors else dirty_rows.append(row)

with open(JSON_PATH, "w", encoding="utf-8") as json_file: 
    json.dump(clean_rows, json_file, indent=2, ensure_ascii=False)

print(f"Errors: {errors}")
print(f"Topics: {seen_topic_dict}")
print(f"Difficulties: {seen_difficulty_dict}")

# Checkpoint

def newJson(topic: str, path: str) -> None: 
    """Take topics with a given name and write them to a new JSON file"""
    topic_qs = []
    for i, row in enumerate(data_list): 
        if row["topic"] == topic: 
            topic_qs.append(row)
    
    with open(path, "w", encoding="utf-8") as f: 
        json.dump(topic_qs, f, indent=2, ensure_ascii=False)

newJson("FHSA", "assignments/checkpoint_fhsa.json")