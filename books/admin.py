from django.contrib import admin

from books.models import Book

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'isbn', 'price']
    list_filter = ['author']
    search_fields = ['title', 'author']
    ordering = ['title']
