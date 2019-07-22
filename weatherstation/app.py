#!/usr/bin/python3

import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 6
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
print("humidity: " + str(humidity))
print("temperature: " + str(temperature))
