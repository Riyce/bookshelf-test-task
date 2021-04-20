from django.db import models


class Book(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120)
    author = models.CharField(verbose_name='Author', max_length=120)
    year = models.IntegerField(verbose_name='Release date')

    class Meta:
        ordering = ['id']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name
