class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}.'

class PaperBook(Book):
    def __init__(self, title, author, numpages):
        Book.__init__(self, title, author)
        self.numpages = numpages

class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size

class Library:
    def __init__(self):
        self.books = []
    def addBook(self, book):
        self.books.append(book)
    def getNumBooks(self):
        return len(self.books)

my_EBook = EBook('the Odyssey', 'Homer', 2)
my_PaperBook = PaperBook('the Odyssey', 'Homer', 500)


all_Books = Library()
all_Books.addBook(PaperBook)
all_Books.addBook(EBook)

print(all_Books.getNumBooks())
