class Book:
    def __init__(self, title, author, year, category, unavailable):
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.unavailable = False

 def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class FictionBook(Book):
     def __init(self, title, author, year):
          super().__init__(title, author, year,"Fiction")


class NonFiction(Book):
     def__init__(self, title, author, year):
     super().__init__(title, author, year, "Non-Fiction")