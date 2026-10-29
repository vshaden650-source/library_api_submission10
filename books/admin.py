from django.contrib import admin

# Register your models here.
from .models import Book, Author, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'isbn', 'available_copies')
    search_fields = ('title', 'isbn')
    list_filter = ('author', 'category', 'published_date')


admin.site.register(Author)
admin.site.register(Category)