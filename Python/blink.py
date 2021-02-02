from time import sleep 
import RPi.GPIO as GPIO

counter = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
while counter <= 10:
	GPIO.output(17, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	sleep(1)
	counter = counter + 1
