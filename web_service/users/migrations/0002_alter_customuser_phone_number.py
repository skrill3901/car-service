# Generated by Django 3.2.16 on 2023-11-26 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='\\+7(\\d{10})')], verbose_name='Номер телефона'),
        ),
    ]
