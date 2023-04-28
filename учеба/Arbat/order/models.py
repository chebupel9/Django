from django.db import models


class Article_order(models.Model):
    title = models.CharField('Название', max_length=50)
    email = models.CharField('Email', max_length=50)
    company = models.CharField('Компания', max_length=100)
    description = models.TextField('Описание')
    date = models.DateField('Дата')
    link = models.CharField('Ссылка', max_length=250)
    username = models.CharField('username', max_length=50)
    name = models.CharField('ФИО', max_length=100)

    def __str__(self):
        return f"Заказ: {self.title}"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
