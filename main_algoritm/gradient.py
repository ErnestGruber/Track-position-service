from math import radians, cos, sin, asin, sqrt, e


# noinspection PyTypeChecker
class Gradient:
    def __init__(self, first_coordinat):
        self.second_coordinat=[]
        self.first_coordinat = first_coordinat
        self.iteration_number = 1
        self.list_S = [1,0]
        self.time =[8, 8]
        self.i=0
    def main(self,second_coordinat):
        self.second_coordinat = second_coordinat
        S = self.get_distance()
        if self.iteration_number==1:
            self.list_S[1]=S
            a= (self.list_S[1] / self.time[1] - self.list_S[0] / self.time[0]) / sum(self.time)
            self.get_time(S, a)
            self.iteration_number=self.iteration_number-1
        if self.iteration_number==0:
            self.list_S[0] = S
            a = (self.list_S[0] / self.time[0] - self.list_S[1] / self.time[1]) / sum(self.time)
            self.get_time(S,a)
            self.iteration_number = self.iteration_number+1
    def get_time(self, S, a):
        if a > 4:
            self.time[self.iteration_number] = self.time[self.iteration_number] *e**(1/3)+2
           # print(a, " speed ", S, "  ", self.time[self.iteration_number])
            return self.time[self.iteration_number]
        if 0 < a < 1:
            self.time[self.iteration_number] = 15
           # print( a , " stabilno  ", S, "  ", self.time[self.iteration_number])
            return self.time[self.iteration_number]
        if a<0:
            self.time[self.iteration_number] = self.time[self.iteration_number] *1/(e**(1/3))+2
           # print(a, " slow  ", S, "  ", self.time[self.iteration_number])
            return self.time[self.iteration_number]

    def get_distance(self):
        R = 6372800
        dLat = radians(self.second_coordinat[0] - self.first_coordinat[0])  # широта2 - широта 1
        dLon = radians(self.second_coordinat[1] - self.first_coordinat[1])  # долгота2-долгта1
        lat1 = radians(self.first_coordinat[0])  # широта1
        lat2 = radians(self.second_coordinat[0])  # широта 2
        a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
        c = 2 * asin(sqrt(a))
        self.first_coordinat = self.second_coordinat
        return R * c

a = Gradient([59.81327946445496, 30.31833866668659])
a.main([59.87685440549503, 30.290872846374086])
a.main([59.89824896312824,30.22976139617877])
a.main([59.9041051265614,30.22289494110071])
a.main([59.90893338872744,30.209848676452214])
a.main([59.93926633835171,30.207102094420968])
a.main([59.945811846332575,30.203668866881912])