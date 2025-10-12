class Book:
    #  Initializes the object
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    #  Runs when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation - for users
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation - for developers
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
