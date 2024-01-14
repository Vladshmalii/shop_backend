from django.contrib import admin
from django import contrib

from . import models as finance_models


# Register your models here.
@contrib.admin.register(finance_models.Transaction)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['price','status']