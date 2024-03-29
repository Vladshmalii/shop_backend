# Generated by Django 4.2.6 on 2024-01-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('status', models.CharField(choices=[('pending', 'Ожидание'), ('completed', 'Завершено')], default='pending', max_length=20, verbose_name='Статус')),
            ],
        ),
    ]
