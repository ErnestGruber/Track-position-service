import time
from main_algoritm.gradient import Gradient

def alg_methods(id, first_coord):
    send_data=Gradient(first_coord, id)
    sqlData=Postgres()
    signal=sqlData.getpoweroneGS(id) #   надо два значени яхороший или не хороший
    while signal>25:
        coordinat_GPS=sqlData.getOneGPS(id) #получить координаты текущие два значения
        t=send_data.main(coordinat_GPS)
        time.sleep(t)
                                # отправить данные T
        simplify_points(getGSM(id),0.01)#то что ты показывал НО ИЗ БАЗЫ ДАННЫХ
    ##    coord_truth=get_average(id) #среднее верно  или нет то что хотел даня
    while signal<=25:
        if sqlData.getpowerwifi(id) >10:
            coordinat_WIFI = wifiapi.mac(sqlData.getMac(id))
            t = send_data.main(coordinat_WIFI)
            time.sleep(t)
        coordinat_GSM=Gsm(GsmApi.getcoord(sqlData.getGSM),GsmApi.getcoord(sqlData.getGSM),-------------).coord()
        t = send_data.main(coordinat_GSM)
        time.sleep(t)
    alg_methods(id, first_coord)


