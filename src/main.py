import Rpi.GPIO as GPIO
import time
LED = 2
LED2 = 4
LED3 = 3
wait = 1
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
while True : 
    GPIO.output(LED, GPIO.HIGH)
    GPIO.output(LED2, GPIO.HIGH)
    GPIO.output(LED3, GPIO.HIGH)
    time.sleep(wait)
    GPIO.output(LED, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    GPIO.output(LED3, GPIO.LOW)
    time.sleep(wait)