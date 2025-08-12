from django.db import models

class Author(models.Model):
    """
    Author model represents a writer of books.

    Fields:
    - name: CharField to store the author's full name.

    Relationship:
    - One author can have many books (one-to-many). The Book model will declare
      a ForeignKey to Author.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book linked to an Author.

    Fields:
    - title: CharField holding the title of the book.
    - publication_year: IntegerField for the year the book was published.
    - author: ForeignKey to Author establishing a one-to-many relationship.

    Notes:
    - `author` uses `on_delete=models.CASCADE` to remove books when an author is deleted.
    - Additional constraints/validators can be added later as needed.
    """

    title = models.CharField(max_length=500)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
