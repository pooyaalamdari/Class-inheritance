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

my_EBook = EBook('the Odyssey', 'Homer', 2)
my_PaperBook = PaperBook('the Odyssey', 'Homer', 500)


print(my_EBook)
print(my_EBook.size)
print('---')
print(my_PaperBook)
print(my_PaperBook.numpages)
