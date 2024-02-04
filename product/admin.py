from django.contrib import admin
from django import contrib
from . import models as product_models


# Register your models here.
@contrib.admin.register(product_models.Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sum_price','status','amount_items']

@contrib.admin.register(product_models.Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','code','color', 'weight', 'height']

@contrib.admin.register(product_models.Supply)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ['items_codes']
