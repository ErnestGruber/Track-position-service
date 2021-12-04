import requests
class GsmApi:

    @staticmethod
    def getcoord(mcc,mnc,cellid,lac):
        response = requests.get(
            f'https://api.mylnikov.org/mobile/main.py/get?mcc={mcc}&mnc={mnc}&cellid={cellid}&lac={lac}&data=open&v=1.1')
        return response.json()['data']['lat'], response.json()['data']['lon']


class Gsm:
    def __init__(self, lat1, lon1, lat2, lon2, lat3, lon3, out1, out2, out3):
        self.x = [lat1, lat2, lat3]
        self.y = [lon1, lon2, lon3]
        self.s = [out1 + 100, out2 + 100, out3 + 100]

    def coord(self):
        w1 = self.s[0] / (self.s[0] + self.s[1] + self.s[2])
        w2 = self.s[1] / (self.s[0] + self.s[1] + self.s[2])
        w3 = self.s[2] / (self.s[0] + self.s[1] + self.s[2])
        x = (w1 * self.x[0] + w2 * self.x[1] + w3 * self.x[2])
        y = (w1 * self.y[0] + w2 * self.y[1] + w3 * self.y[2])
        return (x, y)