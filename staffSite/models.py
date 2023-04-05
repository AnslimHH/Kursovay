from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Наименование')
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы' 

class OrderType(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Наименование')
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип заявки'
        verbose_name_plural = 'Типы заявок' 


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    second_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    order_type = models.ForeignKey(OrderType, verbose_name='Тип отправления',null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=250, verbose_name='Адрес', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'Заявка №{self.id} ({self.user})'


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки' 

