import requests
from json import loads
class gsmapi:
    @staticmethod
    def getcoord(mcc,mnc,cellid,lac):
        response = requests.get(f'https://api.mylnikov.org/mobile/main.py/get?mcc={mcc}&mnc={mnc}&cellid={cellid}&lac={lac}&data=open&v=1.1')
        return response.json()['data']['lat'],response.json()['data']['lon']





class gsm:
    def __init__(self,x1,y1,x2,y2,x3,y3,s1,s2,s3):
        self.x1=x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.s1= s1+100
        self.s2=s2+100
        self.s3=s3+100
    def coord(self):
        w1 = self.s1 / (self.s1 + self.s2 + self.s3)
        w2 = self.s2 / (self.s1 + self.s2 + self.s3)
        w3 = self.s3 / (self.s1 + self.s2 + self.s3)
        x= (w1 * self.x1 + w2 * self.x2 + w3 * self.x3)
        y= (w1 * self.y1 + w2 * self.y2 + w3 * self.y3)
        return (x,y)

