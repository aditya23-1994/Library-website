from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('pk', 'title', 'author', 'body', 'ISBN')

        def validate_title(self, value):
            qs = Book.objects.filter(title__iexact=value)
            
            if qs.exists():
                raise serializers.ValidationError("The title must be Unique")
            return value

class BookRetriveSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('title', 'author', 'body')

class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('title', 'body')

class BookDeleteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('title', 'author', 'body', 'ISBN')
