class Book:
    def __init__(self, title, autohr, price):
        super().__init__()
        self.title = title
        self.author = autohr
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, cost {self.price}"

    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


b1 = Book("Brace New World", "Leo Tolstoy", 1225)
b2 = Book("War and Peace", "JD Salinger", 234)

print(b1)
print(b2)

print(str(b1))
print(repr(b2))