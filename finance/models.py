from django.db import models

# Create your models here.
class Transaction(models.Model):
    price = models.DecimalField(max_digits=20,
                                decimal_places= 2,
                                verbose_name= 'Цена')
    status = models.CharField(max_length= 20,
                              choices=[('pending', 'Ожидание'), ('completed', 'Завершено')],
                              default='pending',
                              verbose_name= 'Статус')