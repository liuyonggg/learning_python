from django.contrib import admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
    fields = ['name', 'pub_date', 'authors']

admin.site.register(Book, BookAdmin)
