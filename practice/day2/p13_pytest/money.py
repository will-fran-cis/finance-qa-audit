# Code under test for Problem 13. Do not change this file until a test tells
# you something is wrong.


def parse_amount(text: str) -> float:
    """Turn text like "$1,250.50" into 1250.5."""
    cleaned = text.strip().replace("$", "").replace(",", "")
    if not cleaned:
        raise ValueError("empty amount")
    amount = float(cleaned)
    if amount < 0:
        raise ValueError(f"negative amount: {amount}")
    return amount


def apply_interest(balance: float, rate_percent: float, years: int) -> float:
    """Compound balance once a year for `years` years, rounded to cents."""
    return round(balance * (1 + rate_percent / 100) ** years, 2)
