class Book:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}>"

    @classmethod
    def hardcovers(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight + 100)

    @classmethod
    def pdf(cls, name, weight):
        return cls(name, cls.pdf_type(), weight + 100)

    @staticmethod
    def pdf_type():
        return "PDF"


book = Book.hardcovers("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
pdf = Book.pdf("Python for pentesters", 1000)

print(book)
print(light)
print(pdf)