from django.contrib import admin
from .models import Category , Book
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['name' , 'author', 'created' , 'img' , 'Categoris' ]
    search_fields = ['name']







