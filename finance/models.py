from django.db import models
from . import choices


class Transaction(models.Model):
    user = models.ForeignKey(to="user.User",
                             on_delete=models.CASCADE,
                             blank=False,
                             null=False)

    order = models.OneToOneField(to="product.Order",
                                 on_delete=models.CASCADE,
                                 blank=False,
                                 null=False)

    price = models.DecimalField(max_digits=20,
                                decimal_places=2,
                                verbose_name='Цена')

    status = models.CharField(max_length=20,
                              choices=choices.statuses,
                              default='pending',
                              verbose_name='Статус')