from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"

b1 = Book("Brace New World", "Leo Tolstoy", 1225, 39.98)
b2 = Book("War and Peace", "JD Salinger", 234, 29.78)
b3 = Book("Brace New World", "Leo Tolstoy", 1225, 39.98)

print(b1.title)
print(b2.author)
print('-------')
print(b1)
print(b1 == b3)
print(b1 == b2)

b1.title = "test123"
b1.pages =1234
print(b1.bookinfo())