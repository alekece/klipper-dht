import board 
import adafruit_dht
import time
import os

READ_INTERVAL = 1
OUTPUT_DIR = "/home/pi/.local/share/dht"

dht = adafruit_dht.DHT11(board.D2)

os.makedirs(OUTPUT_DIR, exist_ok = True)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        os.system("echo {} > {}/temp".format(temperature*1000, OUTPUT_DIR))
        os.system("echo {} > {}/humidity".format(humidity, OUTPUT_DIR))

        print("{}C {}%".format(temperature, humidity))
    except RuntimeError as e:
        print("Cannot read data: {}".format(e))

    time.sleep(READ_INTERVAL)
                                  
