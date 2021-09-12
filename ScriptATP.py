# Carlos Henrique Leister Assunção
from wifi_lib import connect
import machine
import time
import dht
import urequests

DHT11_PIN = 4
RELAY_PIN = 2
SSID = "TP-Link_1428"
PWD = "96875582"
API_WRITE_KEY = "N8TSEB1CQVG02T4D"

# Conecta à rede WiFi
station = connect(SSID, PWD)

# Cria objetos para interagir com os pinos 4 (sensor DHT) e pino 2 (relé, output)
dht = dht.DHT11(machine.Pin(DHT11_PIN))
r = machine.Pin(RELAY_PIN, machine.Pin.OUT)

# Realiza uma medida e imprime na tela os valores de T e U, a cada 15 segundos.
# Se T > 31 ou U > 70, o relé é acionado. Se não, é desligado.

while True:
    dht.measure()
    data = urequests.get(
        "http://api.thingspeak.com/update?api_key={}&field1={}&field2={}".format(API_WRITE_KEY, dht.temperature(),
                                                                                 dht.humidity()))
    data.close()
    print("Temp = {}    Umidade = {}".format(dht.temperature(), dht.humidity()))
    if dht.temperature() > 31 or dht.humidity() > 70:
        r.value(1)
    else:
        r.value(0)
    time.sleep(15)

