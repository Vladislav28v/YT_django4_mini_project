from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Название')
    price = models.IntegerField(verbose_name='Цена')
    description = models.CharField(max_length=200, verbose_name='Описание',)

    class Meta():
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
# Create your models here.
