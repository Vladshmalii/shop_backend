from django.contrib import auth
from django.db import models as django_models
from . import managers as user_managers
# Create your models here.


class User(auth.models.AbstractBaseUser,
           auth.models.PermissionsMixin):
    is_staff = django_models.BooleanField(default=False,
                                          null=False,
                                          blank=False)

    is_active = django_models.BooleanField(default=True,
                                           null=False,
                                           blank=False)

    email = django_models.EmailField(verbose_name="Почта",
                                     unique=True,
                                     null=False,
                                     blank=False)

    name = django_models.CharField(verbose_name="Имя",
                                   max_length=50,
                                   blank=True,
                                   null=True)

    lastname = django_models.CharField(verbose_name="Фамилия",
                                       max_length=50,
                                       blank=True,
                                       null=True)

    avatar = django_models.FileField(upload_to="additional_information/files",
                                     verbose_name="Автар",
                                     null=True,
                                     blank=True)

    born = django_models.DateField(verbose_name="Дата рождения",
                                   blank=True,
                                   null=True)

    # TODO favorites

    USERNAME_FIELD = "email"


    # region             -----Manager-----
    objects = user_managers.CustomAccountManager()
    # endregion