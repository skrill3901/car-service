# Generated by Django 3.2.16 on 2024-01-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_bot_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bot_user_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='id пользователя телеграм'),
        ),
    ]
