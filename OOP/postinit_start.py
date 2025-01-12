from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages}"


b1 = Book("Brace New World", "Leo Tolstoy", 1225, 39.98)
b2 = Book("War and Peace", "JD Salinger", 234, 29.78)

print(b1.description)