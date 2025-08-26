from datetime import datetime

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts associated with this author"""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return all books this author has contracts with"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create a new contract for this author and book"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum of all royalties from this author's contracts"""
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts associated with this book"""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """Return all authors who have contracts with this book"""
        return [c.author for c in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # validations
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return contracts matching the given date, sorted by date"""
        # Filter contracts by the given date
        matching = [c for c in cls.all if c.date == date]
        # Sort by date (even if same, preserve order)
        return sorted(matching, key=lambda c: datetime.strptime(c.date, "%d/%m/%Y"))

