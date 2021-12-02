from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Phone, GPS, GSM, Accelerometr, Gyro, Meta, Req


class PhoneView(APIView):
    def get(self, request):
        phone = Phone.objects.all()
        return Response({"phones": phone})


class GPSView(APIView):
    def get(self, request):
        gps = GPS.objects.all()
        return Response({"gps": gps})


class GSMView(APIView):
    def get(self, request):
        gsm = GSM.objects.all()
        return Response({"gsm": gsm})


class AccelerometrView(APIView):
    def get(self, request):
        accelerometr = Accelerometr.objects.all()
        return Response({"accelerometr": accelerometr})


class GyroView(APIView):
    def get(self, request):
        gyro = Gyro.objects.all()
        return Response({"gyro": gyro})


class MetaView(APIView):
    def get(self, request):
        meta = Meta.objects.all()
        return Response({"meta": meta})


class ReqView(APIView):
    def get(self, request):
        req = Req.objects.all()
        return Response({"req": req})
