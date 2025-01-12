class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, cost {self.price}"

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("Brace New World", "Leo Tolstoy", 39.95)
b2 = Book("War and Peace", "JD Salinger", 29.95)

print(b1)
b1("anna Karenina", "Leo Tilst", 49.90)
print(b1)