# serializers.py
from rest_framework import serializers
from .models import Books_Author, Books_Book, Books_Bookshelf, Books_Language, Books_Subject, Books_Format, Books_Book_Authors, Books_Book_Bookshelves, Books_Book_Languages, Books_Book_Subjects

class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Author
        fields = '__all__'

class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Bookshelf
        fields = '__all__'

class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Language
        fields = '__all__'

class BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Subject
        fields = '__all__'

class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Format
        fields = '__all__'

class BooksBookSerializer(serializers.ModelSerializer):
    authors = BooksAuthorSerializer(many=True, read_only=True)
    bookshelves = BooksBookshelfSerializer(many=True, read_only=True)
    languages = BooksLanguageSerializer(many=True, read_only=True)
    subjects = BooksSubjectSerializer(many=True, read_only=True)
    formats = BooksFormatSerializer(many=True, read_only=True)

    class Meta:
        model = Books_Book
        fields = '__all__'

class BooksBookAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Book_Authors
        fields = '__all__'

class BooksBookBookshelvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Book_Bookshelves
        fields = '__all__'

class BooksBookLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Book_Languages
        fields = '__all__'

class BooksBookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_Book_Subjects
        fields = '__all__'
