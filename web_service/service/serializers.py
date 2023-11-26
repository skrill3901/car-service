from rest_framework import serializers

from users.models import CustomUser
from .models import (Avto,
                     Acceptor,
                     WorkingPrice,
                     Warehouse,
                     Oil,
                     CarModel,
                     Maintenance,
                     Engine,
                     Registration)


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'spare_part', 'price']


class OilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oil
        fields = ['id', 'title', 'viscosity', 'price']


class EngineSerializer(serializers.ModelSerializer):
    oil = serializers.PrimaryKeyRelatedField(queryset=Oil.objects.all())

    class Meta:
        model = Engine
        fields = ['id', 'model', 'oil', 'oil_count', 'engine_vol']


class CarModelSerializer(serializers.ModelSerializer):
    warehouses = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all(), many=True)
    engine = serializers.PrimaryKeyRelatedField(queryset=Engine.objects.all())

    class Meta:
        model = CarModel
        fields = ['id', 'model', 'coef', 'image', 'warehouses', 'engine']


class WorkingPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingPrice
        fields = ['id', 'working_type', 'price']


class AcceptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceptor
        fields = ['id', 'first_name', 'second_name', 'patronim']


class MaintenanceSerializer(serializers.ModelSerializer):
    warehouses = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all(),
                                                    many=True,)
    working_price = serializers.PrimaryKeyRelatedField(queryset=WorkingPrice.objects.all())

    class Meta:
        model = Maintenance
        fields = ['id', 'operation', 'working_time', 'warehouses', 'working_price']


class AvtoSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    car_model = serializers.PrimaryKeyRelatedField(queryset=CarModel.objects.all())

    class Meta:
        model = Avto
        fields = ['id', 'owner', 'vin', 'number', 'sts', 'sold_date', 'mileage', 'car_model']


class RegistrationSerializer(serializers.ModelSerializer):
    acceptor = serializers.PrimaryKeyRelatedField(queryset=Acceptor.objects.all())
    maintenance = serializers.PrimaryKeyRelatedField(queryset=Maintenance.objects.all())
    avto = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Registration
        fields = ['id', 'day', 'time', 'acceptor', 'maintenance', 'avto']
