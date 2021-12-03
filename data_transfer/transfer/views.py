from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Phone, GPS, GSM, Accelerometr, Gyro, Meta, Req
from .serializers import PhoneSerializer, GPSSerializer, GSMSerializer, AccelerometrSerializer, GyroSerializer, MetaSerializer, ReqSerializer


class PhoneView(APIView):
    def get(self, request):
        phone = Phone.objects.all()
        serializer = PhoneSerializer(phone, many=True)
        return Response({"phones": serializer.data})

    def post(self, request):
        phone = request.data.get('phone')
        serializer = PhoneSerializer(data=phone)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "phone '{}' created successfully"})


class GPSView(APIView):
    def get(self, request):
        gps = GPS.objects.all()
        serializer = GPSSerializer(gps, many=True)
        return Response({"gps": serializer.data})

    def post(self, request):
        gps = request.data.get('gps')
        serializer = GPSSerializer(data=gps)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "gps '{}' created successfully"})

class GSMView(APIView):
    def get(self, request):
        gsm = GSM.objects.all()
        serializer = GSMSerializer(gsm, many=True)
        return Response({"gsm": serializer.data})

    def post(self, request):
        gsm = request.data.get('gps')
        serializer = GSMSerializer(data=gsm)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "gsm '{}' created successfully"})


class AccelerometrView(APIView):
    def get(self, request):
        accelerometr = Accelerometr.objects.all()
        serializer = AccelerometrSerializer(accelerometr, many=True)
        return Response({"accelerometr": serializer.data})

    def post(self, request):
        accelerometr = request.data.get('accelerometr')
        serializer = AccelerometrSerializer(data=accelerometr)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "accelerometr '{}' created successfully"})


class GyroView(APIView):
    def get(self, request):
        gyro = Gyro.objects.all()
        serializer = GyroSerializer(gyro, many=True)
        return Response({"gyro": serializer.data})

    def post(self, request):
        gyro = request.data.get('gyro')
        serializer = GyroSerializer(data=gyro)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "gyro '{}' created successfully"})


class MetaView(APIView):
    def get(self, request):
        meta = Meta.objects.all()
        serializer = MetaSerializer(meta, many=True)
        return Response({"meta": serializer.data})

    def post(self, request):
        meta = request.data.get('meta')
        serializer = MetaSerializer(data=meta)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "meta '{}' created successfully"})


class ReqView(APIView):
    def get(self, request):
        req = Req.objects.all()
        serializer = ReqSerializer(req, many=True)
        return Response({"req": serializer.data})

    def post(self, request):
        req = request.data.get('req')
        serializer = ReqSerializer(data=req)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "meta '{}' created successfully"})
