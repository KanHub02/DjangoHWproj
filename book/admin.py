from django.contrib import admin
from book.models import Book,BookComment,BookUser


admin.site.register(Book)
admin.site.register(BookComment)
admin.site.register(BookUser)