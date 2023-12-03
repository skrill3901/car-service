# Generated by Django 3.2.16 on 2023-12-02 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0005_registration_canceled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avto',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='avtos', to='service.carmodel', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='avto',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avtos', to=settings.AUTH_USER_MODEL, verbose_name='Собственник'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carmodels', to='service.engine', verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='engine',
            name='oil',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='engines', to='service.oil', verbose_name='Масло'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintenances', to='service.carmodel', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='working_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintenances', to='service.workingtype', verbose_name='Тип нормо-часа'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='acceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='service.acceptor', verbose_name='Мастер приемщик'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='avto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='service.avto', verbose_name='Автомобиль'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='maintenance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='service.maintenance', verbose_name='Тип ремонта'),
        ),
    ]