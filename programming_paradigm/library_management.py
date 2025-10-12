# library_management.py

class Book:
    """Represents a book with a title, author, and checked-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available for borrowing."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book by title (makes it available again)."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
        """Prints a list of all books currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")
