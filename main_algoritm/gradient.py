from math import radians, cos, sin, asin, sqrt


# noinspection PyTypeChecker
class Gradient:
    def __init__(self, first_coordinat, id_phone):
        self.second_coordinat = []
        self.first_coordinat = first_coordinat
        self.iteration_number = 1
        self.list_S = [0,1]
        self.time = [8, 8]
        self.id = id_phone

    def main(self, second_coordinat):
        self.second_coordinat = second_coordinat
        S = self.get_distance()
        if self.iteration_number == 1:
            self.list_S[1] = S
            a = ((self.list_S[1] / self.time[1]) - (self.list_S[0] / self.time[0])) / sum(self.time)
            self.get_time(S, a)
            self.iteration_number = self.iteration_number - 1
            return
        if self.iteration_number == 0:
            self.list_S[0] = S
            a = ((self.list_S[0] / self.time[0]) - (self.list_S[1] / self.time[1])) / sum(self.time)
            self.get_time(S, a)
            self.iteration_number = self.iteration_number + 1
            return

    def get_time(self, S, a):
        if a > 6:
            self.time[self.iteration_number] = self.time[self.iteration_number] / 1.4
            print("ускоорение = ", a, "\tпуть за прошлый промежуток времени = ", S, "\t через сколько минут запросит снова GPS", self.time[self.iteration_number])
            return self.time[self.iteration_number], self.id
        if 0 < a <=6 :
            self.time[self.iteration_number] = 15
            print(a, " stabilno  ", S, "  ", self.time[self.iteration_number])
            return self.time[self.iteration_number], self.id
        if a < 0:
            self.time[self.iteration_number] = self.time[self.iteration_number] * 1.4
            print("ускоорение = ", a, "\tпуть за прошлый промежуток времени = ", S, "\t через сколько минут запросит снова GPS", self.time[self.iteration_number])
            return self.time[self.iteration_number], self.id

    def get_distance(self):
        R = 6372800
        dLat = radians(self.second_coordinat[0] - self.first_coordinat[0])
        dLon = radians(self.second_coordinat[1] - self.first_coordinat[1])
        lat1 = radians(self.first_coordinat[0])
        lat2 = radians(self.second_coordinat[0])
        a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
        c = 2 * asin(sqrt(a))
        self.first_coordinat = self.second_coordinat
        return R * c


