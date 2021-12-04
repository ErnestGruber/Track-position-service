import time

from GSM.gsm import Gsm, GsmApi
from main_algoritm.gradient import Gradient
from DATA.database import Postgres
import GSM.wifi as WiFi
from main_algoritm.normilized import simplify_points


def alg_methods(id, first_coord):
    send_data = Gradient(first_coord, id)
    sqlData = Postgres()
    signal = sqlData.getpoweroneGS(id)  # надо два значени яхороший или не хороший
    while signal > 25:
        coordinat_GPS = sqlData.getoneGPS(id)  # получить координаты текущие два значения
        t = send_data.main(coordinat_GPS)
        time.sleep(t)
        data = simplify_points(sqlData.getmanyGPS(id), 0.01)
        sqlData.insertgps(data)
    while signal <= 25:
        if sqlData.getpowerwifi(id) > 10:
            coordinat_WIFI = WiFi.wifiapi.getcoord(sqlData.getMac(id))
            t = send_data.main(coordinat_WIFI)
            time.sleep(t)
            w = Postgres.getGSM(1)
            a = GsmApi.getcoord(w[0], w[1], w[2], w[3])
            x1, y1 = a[0], a[1]
            z = Postgres.getGSM(2)
            b = GsmApi.getcoord(z[0], z[1], z[2], z[3])
            x2, y2 = b[0], b[1]
            p = Postgres.getGSM(2)
            c = GsmApi.getcoord(p[0], p[1], p[2], p[3])
            x3, y3 = c[0], c[1]
            x = [x1, x2, x3]
            y = [y1, y2, y3]
            out = Postgres.gsmpower(1)
            a = Gsm(x, y, out)
            coordinat_GSM = a.coord()
        t = send_data.main(coordinat_GSM)
        time.sleep(t)
    alg_methods(id, first_coord)
