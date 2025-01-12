class Book:
    def __init__(self, title, autohr, price):
        super().__init__()
        self.title = title
        self.author = autohr
        self.price = price

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price >= other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price < other.price



b1 = Book("Brace New World", "Leo Tolstoy", 1225)
b2 = Book("War and Peace", "JD Salinger", 234)
b3 = Book("Brace New World", "Leo Tolstoy", 1225)
b4 = Book("War and Peace", "JD Salinger", 234)

# print(b1 == b3)
# print(b1 == b2)

print(b2 >= b1)
print(b2 < b1)

books = [b1, b2, b3, b4]
books.sort()
print([book.title for book in books])