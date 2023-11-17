import RPi.GPIO as GPIO
import signal
import sys
import time

GPIO_ID = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ID, GPIO.OUT)

def exit_handler(signal, frame):
        print("\nExit")
        GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

while True:
        GPIO.output(GPIO_ID, True)
        time.sleep(0.5)
        GPIO.output(GPIO_ID, False)
        time.sleep(0.5)