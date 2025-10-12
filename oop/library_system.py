# Base class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


#  EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"'{self.title}' by {self.author} [EBook, {self.file_size}MB]"


# PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"'{self.title}' by {self.author} [PrintBook, {self.page_count} pages]"


# Library Structure
class Library:
    def __init__(self):
        self.books = []  # list to store all book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def list_books(self):
        print("\nLibrary Collection:")
        for book in self.books:
            print("-", book)
