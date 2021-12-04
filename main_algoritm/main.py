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
        coordinat_GSM = Gsm(GsmApi.getcoord(sqlData.getGSM), GsmApi.getcoord(sqlData.getGSM), sqlData.gsmpower().coord(),1,1,)
        t = send_data.main(coordinat_GSM)
        time.sleep(t)
    alg_methods(id, first_coord)
