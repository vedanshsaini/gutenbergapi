# admin.py
from django.contrib import admin

from books.models import Books_Author, Books_Book, Books_Bookshelf, Books_Language, Books_Subject, Books_Format, Books_Book_Authors, Books_Book_Bookshelves, Books_Book_Languages, Books_Book_Subjects

class BooksBookAuthorInline(admin.TabularInline):
    model = Books_Book_Authors
    extra = 1

class BooksBookBookshelfInline(admin.TabularInline):
    model = Books_Book_Bookshelves
    extra = 1

class BooksBookLanguageInline(admin.TabularInline):
    model = Books_Book_Languages
    extra = 1

class BooksBookSubjectInline(admin.TabularInline):
    model = Books_Book_Subjects
    extra = 1

class BooksFormatInline(admin.TabularInline):
    model = Books_Format
    extra = 1

class BooksBookAdmin(admin.ModelAdmin):
    inlines = [BooksBookAuthorInline, BooksBookBookshelfInline, BooksBookLanguageInline, BooksBookSubjectInline, BooksFormatInline]
    list_display = ('title', 'download_count', 'gutenberg_id', 'media_type')
    search_fields = ('title',)

admin.site.register(Books_Author)
admin.site.register(Books_Book, BooksBookAdmin)
admin.site.register(Books_Bookshelf)
admin.site.register(Books_Language)
admin.site.register(Books_Subject)
