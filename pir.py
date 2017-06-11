import RPi.GPIO as GPIO
import time, OSC, conf

ON = "ON"
OFF = "OFF"

PIR_PIN = 26

def on_transition_cb(channel):

	if GPIO.input(channel) == 1:
		print "transition -- ON"
	else 
		print "transition -- OFF"

if __name__ == "__main__":

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIR_PIN, GPIO.IN)

	GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, on_transition_cb, bouncetime=1000)

	try:
		while True:
			time.sleep(3)
	except Exception as e:
		raise
	finally:
		GPIO.cleanup()

