# Problem 12 (dataclasses) - easy
from dataclasses import dataclass
from dataclasses import field
#
# Part A. Write a dataclass Holding with fields:
#   ticker: str, units: int, price: float
# and one method value(self) -> float that returns units * price.
# Do NOT write __init__. Let @dataclass generate it.

@dataclass
class Holding: 
    ticker: str
    units: int
    price: float

    def value(self) -> float: 
        return self.units * self.price


# Part B. Write a dataclass Portfolio with fields:
#   owner: str
#   holdings: list[Holding], defaulting to an empty list
# and methods:
#   add(self, holding: Holding) -> None    appends to holdings
#   total(self) -> float                   sum of every holding's value()
# For the default, look up field() and default_factory in the dataclasses
# docs (section "Mutable default values").


@dataclass
class Portfolio: 
    owner: str
    holdings: list[Holding] = field(default_factory=list)

    def add(self, holding: Holding) -> None: 
        self.holdings.append(holding)

    def total(self) -> float: 
        sum = 0
        for holding in self.holdings: 
            sum += holding.value()
        return sum

# Part C. In main() under a guard:
#   h = Holding("XIC", 10, 35.5)
#   print(h)
#   print(h == Holding("XIC", 10, 35.5))
#   print(h.value())
#   p1 = Portfolio("Ana");  p2 = Portfolio("Ben")
#   p1.add(h);  p1.add(Holding("VFV", 2, 120.0))
#   print(p1.total())
#   print(p2)

def main(): 
    h = Holding("XIC", 10, 35.5)
    print(h)
    print(h == Holding("XIC", 10, 35.5))
    print(h.value())
    p1 = Portfolio("Ana");  p2 = Portfolio("Ben")
    p1.add(h);  p1.add(Holding("VFV", 2, 120.0))
    print(p1.total())
    print(p2)

# Expected output:
# Holding(ticker='XIC', units=10, price=35.5)
# True
# 355.0
# 595.0
# Portfolio(owner='Ben', holdings=[])
#
# Experiments after it works (no need to write anything down):
#   1. Compare print(h) here with print(a) in p09. Which method did
#      @dataclass write that your Account didn't have? And for `==`?
#   2. Change the holdings default to a plain `= []` and run. Read the error.
#      This is the p10 / Day 1 mutable default bug, caught for you.
#   3. Try Holding("XIC", "ten", 35.5). Does creating it fail? Now call
#      .value() on it. What does this tell you about whether a dataclass
#      checks types? Who will have to check them in today's loader.py?

# Your code below
if __name__ == "__main__": 
    main()