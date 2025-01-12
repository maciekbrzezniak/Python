from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))
@dataclass
class Book:
    title: str = "No title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)

b1 = Book()
print(b1)

b2 = Book("War and Peace", "JD Salinger", 234)
b3 = Book("Brace New World", "Leo Tolstoy", 1225)

print(b2)
print(b3)