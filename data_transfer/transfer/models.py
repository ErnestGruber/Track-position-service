from django.db import models


class Phone(models.Model):
    id_phone = models.FloatField() #  уник номер


class GPS(models.Model):
    id_phone = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()


class GSM(models.Model):
    id_phone = models.TextField()
    power = models.FloatField()
    id_tower = models.FloatField()


class Accelerometr(models.Model):
    id_phone = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()


class Gyro(models.Model):
    id_phone = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()


class Meta(models.Model):
    id_phone = models.TextField()
    volt = models.IntegerField()


class Req(models.Model):
    id_req = models.IntegerField()
    time = models.DateTimeField()
