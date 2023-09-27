import Adafruit_DHT
import time
import pyrebase

config = {
    "apiKey": "AIzaSyCb****5VIfJN******IF0Uv4udINwAfOlU",
    "authDomain": "rasp***y.firebaseapp.com",
    "databaseURL": "https://ra***r-***c-default-rtdb.fire**seio.com/",
    "storageBucket": "gs://ra****y-8d***c.ap**t.com/"}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

sensor = Adafruit_DHT.DHT11

pin = 21

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        data = {"Temperature" : temperature, "Humidity" : humidity}
        db.child("Status").push(data)
        db.update(data)
        print("Sent to Firebase")
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)
