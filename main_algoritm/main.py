from main_algoritm.gradient import Gradient


def alg_methods(id, first_coord):
    send_data=Gradient(first_coord, id)
    signal=get_signal_GPS(id) #   надо два значени яхороший или не хороший
    while signal==norm or average==True:
        coord=get_coord() #получить координаты текущие два значения
        send_data.main(coord)
        normalize() #то что ты показывал НО ИЗ БАЗЫ ДАННЫХ
        coord_truth=get_average(id) #среднее верно  или нет то что хотел даня
    while signal==not_norm and coord_truth()== False:
        while wifi_connection(id)==True:
            send_data = wifiapi()
            send_data.wifiapi()
            coord_truth = get_average(id)
        get_datagsm
        coord_truth = get_average(id)
    alg_methods(id, first_coord)


