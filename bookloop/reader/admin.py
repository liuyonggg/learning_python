from django.contrib import admin
from reader.models import FriendShip, Book, ReadBook

# Register your models here.

class FriendShipAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class ReadBookAdmin(admin.ModelAdmin):
    pass

admin.site.register(FriendShip, FriendShipAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(ReadBook, ReadBookAdmin)
