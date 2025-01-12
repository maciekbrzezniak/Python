from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self, other):
        pass

@dataclass
class Stock(Asset):
    ticker: str
    company: str

    def __lt__(self, other):
        return self.price < other.price

@dataclass
class Bond(Asset):
    description: str
    duration: str
    yieldamt: float

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt

stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock('META', 275.0, "Meta Paltforms Inc"),
    Stock("AMZN", 135.0, "Amazon Inc"),
]

bonds = [
    Bond(95.31, "30 years us treasury", 30, 4.38),
    Bond(96.70, "10 years us treasury", 10, 4.28),
    Bond(98.65, "5 years us treasury", 5, 4.43),
    Bond(99.57, "2 years us treasury", 2, 4.98),
]

try:
    ast = Asset(100.0)
except:
    print("can't instatntaie asset!")

stocks.sort()
bonds.sort()
for stock in stocks:
    print(stock)
print("----------")
for bond in bonds:
    print(bond)