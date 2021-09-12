def connect(ssid, pwd):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, pwd)

    for t in range(50):
        if station.isconnected():
            print("Conectado: ", ssid)
            break
        time.sleep(0.1)
    return station
