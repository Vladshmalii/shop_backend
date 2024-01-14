from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.TextField()

class Order(models.Model):
    items = models.CharField(max_length= 20,
                             blank=False,
                             null=False,
                             verbose_name='Товар')
    amound_items = models.PositiveIntegerField(blank= False,
                                               null= False,
                                               verbose_name='Кол. Товаров')
    sum_price = models.DecimalField(max_digits=20,
                                    decimal_places=2,
                                    blank=False,
                                    null=False,
                                    verbose_name='Сумма',
                                    )

    status = models.CharField(max_length= 20,
                              choices=[('pending', 'Ожидание'),
                                       ('processing', 'Обработка'),
                                       ('completed', 'Завершено'),
                                       ('canceled', 'Отменено'),
                                       ],
                              default= 'pending',
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
                                    verbose_name='Цена')
        code = models.PositiveIntegerField(blank=False,
                                           null=False,
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
        items_codes = models.DecimalField(max_digits=20,
                                          decimal_places=2,
                                          blank=False,
                                          null=False,
                                          verbose_name='Код товаров:Количество')
