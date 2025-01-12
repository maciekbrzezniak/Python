
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)

class Newspapper(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspapper("NY Times", "NY Times Company", "Daily", 6.0)
m1 = Magazine("Scientific American", "Springer Nature", "monthly", 5.99)

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)