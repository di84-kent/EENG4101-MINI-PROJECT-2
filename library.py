class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def view_book(self):
        if not self.books:
            print("There are no books in this library :(")

        for book in self.books:
            print(f"{self.title} by {self.author} in the year {self.year}")
            