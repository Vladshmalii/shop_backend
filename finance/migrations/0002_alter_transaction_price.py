# Generated by Django 4.2.6 on 2024-01-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена'),
        ),
    ]