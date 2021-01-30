from time import sleep 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
while True:
	GPIO.output(17, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	sleep(1)
