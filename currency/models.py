from django.db import models

# Create your models here.
class Currency(models.Model):
    cur_id = models.AutoField(primary_key=True, verbose_name='ID валюты')
    name = models.CharField(max_length=100, verbose_name='Название валюты')
    rate = models.FloatField(verbose_name='Курс валюты')
    charcode = models.CharField(max_length=6, verbose_name='Код валюты')
    nominal = models.IntegerField(verbose_name='Номинал')

    def __str__(self):
        return f'{self.cur_id} - {self.charcode}'