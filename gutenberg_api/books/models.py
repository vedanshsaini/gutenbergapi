# models.py
from django.db import models

class Books_Author(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Books_Book(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    download_count = models.IntegerField(null=True, blank=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField()
    authors = models.ManyToManyField(Books_Author, through='Books_Book_Authors', related_name='books')
    bookshelves = models.ManyToManyField('Books_Bookshelf', through='Books_Book_Bookshelves', related_name='books')
    languages = models.ManyToManyField('Books_Language', through='Books_Book_Languages', related_name='books')
    subjects = models.ManyToManyField('Books_Subject', through='Books_Book_Subjects', related_name='books')

    def __str__(self):
        return self.title

class Books_Book_Authors(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Books_Book, on_delete=models.CASCADE, related_name='book_authors')
    author = models.ForeignKey(Books_Author, on_delete=models.CASCADE, related_name='book_authors')

    class Meta:
        unique_together = ('book', 'author')

    def __str__(self):
        return f"Book: {self.book}, Author: {self.author}"

class Books_Book_Bookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Books_Book, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey('Books_Bookshelf', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'bookshelf')

class Books_Book_Languages(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Books_Book, on_delete=models.CASCADE)
    language = models.ForeignKey('Books_Language', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'language')

class Books_Book_Subjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Books_Book, on_delete=models.CASCADE)
    subject = models.ForeignKey('Books_Subject', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'subject')

class Books_Bookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Books_Format(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(Books_Book, on_delete=models.CASCADE, related_name='formats')

    def __str__(self):
        return self.mime_type

class Books_Language(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.code

class Books_Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name
