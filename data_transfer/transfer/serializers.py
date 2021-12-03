from rest_framework import serializers
from .models import Phone, GPS, GSM, Accelerometr, Gyro, Meta, Req

class PhoneSerializer(serializers.Serializer):
    id_phone = serializers.FloatField()

    def create(self, validated_data):
        return Phone.objects.create(**validated_data)


class GPSSerializer(serializers.Serializer):
    id_phone = serializers.CharField()
    lat = serializers.FloatField()
    lon = serializers.FloatField()

    def create(self, validated_data):
        return GPS.objects.create(**validated_data)


class GSMSerializer(serializers.Serializer):
    id_phone = serializers.CharField()
    power = serializers.FloatField()
    id_tower = serializers.FloatField()

    def create(self, validated_data):
        return GSM.objects.create(**validated_data)


class AccelerometrSerializer(serializers.Serializer):
    id_phone = serializers.CharField()
    x = serializers.FloatField()
    y = serializers.FloatField()
    z = serializers.FloatField()

    def create(self, validated_data):
        return Accelerometr.objects.create(**validated_data)


class GyroSerializer(serializers.Serializer):
    id_phone = serializers.CharField()
    x = serializers.FloatField()
    y = serializers.FloatField()
    z = serializers.FloatField()

    def create(self, validated_data):
        return Gyro.objects.create(**validated_data)


class MetaSerializer(serializers.Serializer):
    id_phone = serializers.CharField()
    volt = serializers.IntegerField()

    def create(self, validated_data):
        return Meta.objects.create(**validated_data)


class ReqSerializer(serializers.Serializer):
    id_req = serializers.IntegerField()
    time = serializers.DateTimeField()

    def create(self, validated_data):
        return Req.objects.create(**validated_data)
