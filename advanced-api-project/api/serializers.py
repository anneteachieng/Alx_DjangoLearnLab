from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    - Serializes all fields of Book.
    - Implements a custom `validate_publication_year` method to ensure the
      year is not in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id']

    def validate_publication_year(self, value):
        """
        Ensure the publication_year is not greater than the current year.
        This runs on single-field validation.

        Raises:
            serializers.ValidationError: if `value` is in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    A compact serializer used for nested representation inside the AuthorSerializer.
    We present only essential fields when nested, but you could reuse BookSerializer
    if you prefer the full representation.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    - Includes the `name` field from Author.
    - Includes a nested list of related books using NestedBookSerializer.
    - The nested `books` field is read-only by default here. If you want to create
      books while creating/updating authors, you'd implement `create` and `update`
      to handle nested writes (example included below as comments).
    """

    # `books` is obtained from the related_name on Book.author (`related_name='books'`).
    books = NestedBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        read_only_fields = ['id']
