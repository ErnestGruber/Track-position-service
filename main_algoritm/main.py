from main_algoritm.gradient import Gradient


def alg_methods(id, first_coord):
    send_data=Gradient(first_coord, id)
    signal=get_signal(id)
    coord_truth(id)
    while signal==norm or coord_truth()==True:
        coord=get_coord()
        send_data.main(coord)
        normalize()
        if signal==norm or coord_truth()==True:
            get_average()
    while signal==not_norm and coord_truth()== False:
        while wifi_connection(id)==True:
            send_data = wifiapi()
            send_data.wifiapi()
        get_datagsm
    alg_methods(id,first_coord)

