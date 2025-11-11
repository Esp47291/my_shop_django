# library/admin.py
from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date') # Поля для отображения в списке
    list_filter = ('birth_date',) # Фильтрация по дате рождения
    search_fields = ('first_name', 'last_name') # Поиск по имени и фамилии
    ordering = ['last_name'] # Сортировка по умолчанию

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date') # Поля для отображения в списке
    list_filter = ('author', 'publication_date') # Фильтрация по автору и дате
    search_fields = ('title', 'author__last_name') # Поиск по названию и фамилии автора
    ordering = ['title'] # Сортировка по умолчанию