import requests
class GsmApi:

    @staticmethod
    def getcoord(mcc,mnc,lac,cellid):
        response = requests.get(
            f'https://api.mylnikov.org/geolocation/cell?v=1.1&data=open&mcc={mcc}&mnc={mnc}&lac={lac}&cellid={cellid}')
        return response.json()['data']['lat'], response.json()['data']['lon']


class Gsm:
    def __init__(self, x, y, out):
        self.x = x
        self.y = y
        self.s = [x+100 for x in out]

    def coord(self):
        w1 = self.s[0] / (self.s[0] + self.s[1] + self.s[2])
        w2 = self.s[1] / (self.s[0] + self.s[1] + self.s[2])
        w3 = self.s[2] / (self.s[0] + self.s[1] + self.s[2])
        x = (w1 * self.x[0] + w2 * self.x[1] + w3 * self.x[2])
        y = (w1 * self.y[0] + w2 * self.y[1] + w3 * self.y[2])
        return (x, y)

