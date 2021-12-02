from math import radians, cos, sin, asin, sqrt

class Gradient:
    def __init__(self, second_coordinat):
        self.second_coordinat=second_coordinat
        self.first_coordinat=second_coordinat
    def main(self):

    def get_distance(self):
        R = 6372.8
        dLat = radians(self.second_coordinat[0] - self.first_coordinat[0])   #широта2 - широта 1
        dLon = radians(self.second_coordinat[1] - self.first_coordinat[1])   #долгота2-долгта1
        lat1 = radians(self.first_coordinat[0])       #широта1
        lat2 = radians(self.second_coordinat[0])        #широта 2
        a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
        c = 2 * asin(sqrt(a))
        self.first_coordinat=self.second_coordinat
        return R * c

