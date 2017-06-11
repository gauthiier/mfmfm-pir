import RPi.GPIO as GPIO
import time, OSC, conf

ON = "ON"
OFF = "OFF"

PIR_PIN = 26

def on_falling_transition_cb(channel):
	print "transition -- OFF"

def on_rising_transition_cb(channel):
	print "transition -- ON"

if __name__ == "__main__":

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIR_PIN, GPIO.IN)

	GPIO.add_event_detect(PIR_PIN, GPIO.FALLING, on_falling_transition_cb, bouncetime=1000)
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, on_rising_transition_cb, bouncetime=1000)

	try:
		while True:
			time.sleep(3)
	except Exception as e:
		raise
	finally:
		GPIO.cleanup()

