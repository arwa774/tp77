import machine
import time
import urequests
import net
import random
import network 
import time

def wifi_connect():  
    print("Connecting to WiFi", end="")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("iPhone de arwa","arwahm156")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(0.1)
    print(" Connected to : ") ; print(wlan.ifconfig())
    
wifi_connect()
'''def send_alert():
    data = " Motion detected "
    response = urequests.post(url, json=data)
net.wifi_connect()
# Configuration du capteur de mouvement PIR
PIR_PIN = machine.Pin(17, machine.Pin.IN)
# Configuration de l'URL de votre site ntfy.sh
url = 'https://ntfy.sh/th-panne'
def send_alert():
    data = " Motion detected "
    response = urequests.post(url, json=data)
net.wifi_connect()
# Configuration du capteur de mouvement PIR
PIR_PIN = machine.Pin(17, machine.Pin.IN)
# Configuration de l'URL de votre site ntfy.sh
url = 'https://ntfy.sh/th-test' '''