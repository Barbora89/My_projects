

class Book:
    def __init__(self,title,author,pages,is_read = False):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def mark_as_read(self):
         self.is_read = True

    def get_info(self):
        return f"{self.title} od {self.author}, {self.pages}"

    def time_to_read(self):
        return f" this book will take {self.pages * 2} minutes"


book_1 = Book("Starec a more", "Hemingway", 400, False)
book_2 = Book("Sbohem armado", "Remarque", 300, True)
book_3 = Book("Tri sestry", "Cechov", 200, False)

print(book_1.get_info(),book_1.time_to_read())
print(book_2.get_info(),book_2.time_to_read() )
print(book_3.get_info(), book_3.time_to_read())