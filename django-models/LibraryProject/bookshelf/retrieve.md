#retrieve

>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> print(books)

<QuerySet [<Book: 1984 by George Orwell (1949)>]>
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949
