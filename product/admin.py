from django.contrib import admin
from django import contrib
from . import models as product_models


# Register your models here.
@contrib.admin.register(product_models.Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['items','sum_price','status','amound_items']

@contrib.admin.register(product_models.Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','code','color', 'weight', 'height']

@contrib.admin.register(product_models.Supply)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['items_codes']
