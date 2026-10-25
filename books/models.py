from django.db import models


# Create your models


class Category(models.Model):
    name = models.CharField('table name',max_length=100)
    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name




class Book(models.Model):
    Categoris = models.ForeignKey('Category',verbose_name='table', blank=True , on_delete=models.CASCADE , null=True)
    name = models.CharField('Book name',max_length=100)
    text = models.TextField(verbose_name='book information')
    author = models.CharField('author',max_length=100 )
    img = models.ImageField('book picture',upload_to='images/' , blank=True)
    created = models.IntegerField(verbose_name='created' , blank=True)

    class Meta:
        db_table = 'book'
        verbose_name = 'book'
        verbose_name_plural = 'books'


    def __str__(self):
        return self.name