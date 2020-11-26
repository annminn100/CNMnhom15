import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
broker="192.168.137.149"
port=1883
def on_publish(client,userdata,result):
    print("data published \n")
    pass
while True:
    client1=paho.Client("control")
    client1.on_publish=on_publish
    client1.connect(broker,port)
    GPIO.output(18, GPIO.HIGH)
    ret=client1.publish("menu/led1","led do on")
    time.sleep(0.5)
    GPIO.output(18, GPIO.LOW)
    ret=client1.publish("menu/led1","led do off")
    time.sleep(0.5)

