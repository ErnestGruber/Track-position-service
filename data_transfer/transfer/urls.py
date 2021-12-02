from django.urls import path
from .views import PhoneView, GPSView, GSMView, AccelerometrView, GyroView, MetaView, ReqView


app_name = "transfer"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('phones/', PhoneView.as_view()),
    path('gps/', GPSView.as_view()),
    path('gsm/', GSMView.as_view()),
    path('accel/', AccelerometrView.as_view()),
    path('gyro/', GyroView.as_view()),
    path('meta/', MetaView.as_view()),
    path('req/', ReqView.as_view())
]