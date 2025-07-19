from relationship_app.models import Author, Book, Library, Librarian

author_name = "Susanna Gregory"
books = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books:
    print(f"- {book.title}")

library_name = "Mystery Archives"
library = Library.objects.get(name=library_name)
print(f"\nBooks in library '{library_name}':")
for book in library.books.all():
    print(f"- {book.title}")

print(f"\nLibrarian of library '{library_name}': {library.librarian.name}")

