# Code under test for Problem 14. This file has no known bugs.

import csv


def load_rates(path: str) -> dict[str, float]:
    """Read a CSV with columns date,rate and return {date: rate}."""
    rates: dict[str, float] = {}
    with open(path, encoding="utf-8", newline="") as f:
        for row_number, row in enumerate(csv.DictReader(f), start=2):
            try:
                rates[row["date"]] = float(row["rate"])
            except ValueError as err:
                raise ValueError(f"row {row_number}: bad rate {row['rate']!r}") from err
    if not rates:
        raise ValueError("no rates in file")
    return rates