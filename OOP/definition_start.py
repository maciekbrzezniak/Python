class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    __booklist = None

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'Secret attribute'
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

print("Book types: ", Book.get_book_types())

book1 = Book("Brace New World", "Leo Tolstoy", 1225, 39.95, "HARDCOVER")
book2 = Book("War and Peace", "JD Salinger", 234, 29.95, "EBOOK")

# print(book1.getprice())

book2.setdiscount(0.25)
# print(book2.getprice())

# print(book2._Book__secret)

print(type(book1) == type(book2))
print(isinstance(book2,Book))
print(isinstance(book2,object))

thebooks = Book.getbooklist()
thebooks.append(book1)
thebooks.append(book2)

print(thebooks)