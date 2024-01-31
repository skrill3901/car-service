# Generated by Django 3.2.16 on 2023-12-23 13:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0014_alter_carmodel_compatible_engines'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avto',
            new_name='Car',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='avto',
            new_name='car',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='canceled',
        ),
    ]
