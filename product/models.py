from django.db import models
from django.core import validators
# Create your models here.

from . import choices


class Order(models.Model):
    items = models.ManyToManyField(to="product.Item",
                                   verbose_name='Товары')

    user = models.ForeignKey(to="user.User",
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)

    amount_items = models.PositiveIntegerField(blank=False,
                                               null=False,
                                               verbose_name='Кол. Товаров')

    sum_price = models.DecimalField(max_digits=20,
                                    decimal_places=2,
                                    blank=False,
                                    null=False,
                                    validators=[validators.MinValueValidator(1)],
                                    verbose_name='Сумма')

    status = models.CharField(max_length=20,
                              choices=choices.statuses,
                              default='pending',
                              verbose_name='Статус')


class Item(models.Model):
    title = models.CharField(max_length=50,
                             blank=False,
                             null=False,
                             verbose_name='Название')

    price = models.DecimalField(max_digits=20,
                                decimal_places=2,
                                blank=False,
                                null=False,
                                validators=[validators.MinValueValidator(1)],
                                verbose_name='Цена')

    code = models.PositiveIntegerField(blank=False,
                                       null=False,
                                       unique=True,
                                       verbose_name='Код')

    color = models.CharField(max_length=20,
                             blank=False,
                             null=False,
                             verbose_name='Цвет')

    weight = models.PositiveIntegerField(blank=False,
                                         null=False,
                                         verbose_name='Масса')

    height = models.PositiveIntegerField(blank=False,
                                         null=False,
                                         verbose_name='Высота')

    width = models.PositiveIntegerField(blank=False,
                                        null=False,
                                        verbose_name='Ширина')


class Supply(models.Model):
    items_codes = models.JSONField(blank=True,
                                   null=True,
                                   verbose_name='Код товаров:Количество')
