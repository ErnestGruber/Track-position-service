from django.contrib import admin
from .models import Phone, GPS, GSM, Accelerometr, Gyro, Meta, Req

admin.site.register(Phone)
admin.site.register(GPS)
admin.site.register(GSM)
admin.site.register(Accelerometr)
admin.site.register(Gyro)
admin.site.register(Meta)
admin.site.register(Req)
# Register your models here.
