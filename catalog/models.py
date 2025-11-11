from django.db import models

# Create your models here.
# catalog/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение') # Требует Pillow
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена покупки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

# Pillow нужно установить: pip install Pillow
# и добавить в settings.MEDIA_URL, MEDIA_ROOT и urls.py (см. ниже)

# library/models.py
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name']

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    publication_date = models.DateField(verbose_name='Дата публикации', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title']