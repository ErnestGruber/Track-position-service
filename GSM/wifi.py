import requests
class wifiapi:
    @staticmethod
    def getcoord(mac):
        response = requests.get(f' https://api.mylnikov.org/geolocation/wifi?v=1.1&bssid={mac}&data=open')
        return response.json()['data']['lat'],response.json()['data']['lon']

print(wifiapi.getcoord('00:0C:42:1F:65:E9'))