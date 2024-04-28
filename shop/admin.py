from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']
    list_filter = ['price']
    list_per_page = 10
    list_editable = ['price']
