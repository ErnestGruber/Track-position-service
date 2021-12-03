import requests
class gsmapi:
    @staticmethod
    def getcoord(mcc,mnc,cellid,lac):
        response = requests.get(f'https://api.mylnikov.org/mobile/main.py/get?mcc={mcc}&mnc={mnc}&cellid={cellid}&lac={lac}&data=open&v=1.1')
        print(response.json())
gsmapi.getcoord('250','02','48181','1671')


class gsm:
    def __init__(self,x1,y1,x2,y2,x3,y3,s1,s2,s3):
        self.x1=x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.s1= abs(s1)
        self.s2=abs(s2)
        self.s3=abs(s3)
    def coord(self):
        w1 = self.s1 / (self.s1 + self.s2 + self.s3)
        w2 = self.s2 / (self.s1 + self.s2 + self.s3)
        w3 = self.s3 / (self.s1 + self.s2 + self.s3)
        x= (w1 * self.x1 + w2 * self.x2 + w3 * self.x3)
        y= (w1 * self.y1 + w2 * self.y2 + w3 * self.y3)
        return (x,y)

