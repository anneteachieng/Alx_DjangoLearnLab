from relationship_app.models import Author, Book, Library

# Query all books by a specific author
author_name = "Susanna Gregory"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
library_name = "Mystery Archives"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian = library.librarian  # thanks to OneToOneField related_name='librarian'
print(f"\nLibrarian of {library_name}: {librarian.name}")

