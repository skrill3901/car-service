# Generated by Django 3.2.16 on 2023-11-20 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronim', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17, unique=True, verbose_name='VIN')),
                ('number', models.CharField(blank=True, max_length=9, unique=True, verbose_name='Госномер')),
                ('sts', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Номер свидетельства о регистрации')),
                ('sold_date', models.DateField(blank=True, verbose_name='Дата продажи')),
                ('mileage', models.IntegerField(verbose_name='Пробег')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, unique=True, verbose_name='Модель')),
                ('image', models.CharField(max_length=100)),
                ('coef', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Коэффициент')),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, unique=True, verbose_name='Модель')),
                ('oil_count', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Количество масла')),
                ('engine_vol', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Объём двигателя')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=150, unique=True, verbose_name='Операция')),
                ('working_time', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Количество нормо-часов')),
            ],
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Масло')),
                ('viscosity', models.CharField(max_length=7, verbose_name='Вязкость')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_part', models.CharField(max_length=150, unique=True, verbose_name='Запчасть')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_type', models.CharField(max_length=50, unique=True, verbose_name='Тип нормочаса')),
                ('price', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Стоимость нормочаса')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('acceptor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.acceptor', verbose_name='Мастер приемщик')),
                ('avto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.avto', verbose_name='Автомобиль')),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.maintenance', verbose_name='Тип ремонта')),
            ],
        ),
        migrations.AddConstraint(
            model_name='oil',
            constraint=models.UniqueConstraint(fields=('title', 'viscosity'), name='oil_uq'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='warehouses',
            field=models.ManyToManyField(to='service.Warehouse', verbose_name='Запасные части'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='working_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.workingprice', verbose_name='Предварительная стоимость'),
        ),
        migrations.AddField(
            model_name='engine',
            name='oil',
            field=models.ManyToManyField(blank=True, to='service.Oil'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='engine',
            field=models.ManyToManyField(to='service.Engine'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='warehouses',
            field=models.ManyToManyField(blank=True, to='service.Warehouse'),
        ),
        migrations.AddField(
            model_name='avto',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.carmodel', verbose_name='Модель автомобиля'),
        ),
        migrations.AddField(
            model_name='avto',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Собственник'),
        ),
    ]
