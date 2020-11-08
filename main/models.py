from django.db import models
from django.db import models

class Ak(models.Model):
    types = models.CharField('Заголовок', max_length=250)
    txt = models.TextField('Текст')
    sk = models.CharField('Промо код', max_length=250, default="") 
    typesen = models.CharField('Title', max_length=250,default="")
    txten = models.TextField('Text',default="")
    sken = models.CharField('Promo code', max_length=250,default="")
    def __str__(self):
        return self.types

# Create your models here.
