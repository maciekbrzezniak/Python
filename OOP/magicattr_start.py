class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, cost {self.price}"

    def __getattribute__(self, item):
        if item == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p * d)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key == 'price':
            if type(value) is not float:
                raise ValueError("The 'price' attr must be a float")
        return super().__setattr__(key,value)

    def __getattr__(self, item):
        return item + " is not here!"

b1 = Book("Brace New World", "Leo Tolstoy", 39.95)
b2 = Book("War and Peace", "JD Salinger", 29.95)

b1.price = 40.0
print(b1.randaomprop)