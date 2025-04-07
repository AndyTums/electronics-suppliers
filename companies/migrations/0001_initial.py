# Generated by Django 5.1.7 on 2025-03-29 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название компании')),
                ('category', models.CharField(choices=[('factory', 'Производство с завода'), ('retail', 'Розничная продажа'), ('individual entrepreneur', 'Индивидуальный предприниматель')], verbose_name='Вид деятельности')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('duty_supplier', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.company', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
    ]
