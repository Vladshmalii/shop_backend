from django.contrib import admin
from django import contrib

from . import models as user_models
# Register your models here.


@contrib.admin.register(user_models.User)
class UserAdmin(contrib.admin.ModelAdmin):
    list_display = ["id", "email", "name", "lastname"]
