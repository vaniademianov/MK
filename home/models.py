from django.db import models

class Ak(models.Model):
    types = models.CharField('Заголовок', max_length=250)
    txt = models.TextField('Текст')
    def __str__(self):
        return self.types

# Create your models here.