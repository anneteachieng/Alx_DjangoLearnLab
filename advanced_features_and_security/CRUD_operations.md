#CRUD Operations for Book Model

#create

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984>

#RETRIEVE

>>> books = Book.objects.all()
>>> for book in books:
...     print(book.id, book.title, book.author, book.publication_year)
...
1 1984 George Orwell 1949

#UPDATE

>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four>

#DELETE

>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})

>>> Book.objects.all()
<QuerySet []>
