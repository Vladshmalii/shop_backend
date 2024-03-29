# Generated by Django 4.2.6 on 2024-01-22 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена')),
                ('code', models.PositiveIntegerField(unique=True, verbose_name='Код')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
                ('weight', models.PositiveIntegerField(verbose_name='Масса')),
                ('height', models.PositiveIntegerField(verbose_name='Высота')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_codes', models.JSONField(blank=True, null=True, verbose_name='Код товаров:Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_items', models.PositiveIntegerField(verbose_name='Кол. Товаров')),
                ('sum_price', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Сумма')),
                ('status', models.CharField(choices=[('pending', 'Ожидание'), ('processing', 'Обработка'), ('completed', 'Завершено'), ('canceled', 'Отменено')], default='pending', max_length=20, verbose_name='Статус')),
                ('items', models.ManyToManyField(to='product.item', verbose_name='Товары')),
            ],
        ),
    ]
