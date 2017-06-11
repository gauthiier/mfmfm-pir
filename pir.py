import RPi.GPIO as GPIO
import time, OSC, conf

ON = "ON"
OFF = "OFF"
PIR_PIN = 26

connected = False
client = OSC.OSCClient()

def on_transition_cb(channel):

	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress(conf.MOUNT)	
	msg = ''

	if GPIO.input(channel) == 1:
		print "transition -- ON"
		msg = ON
	else:
		print "transition -- OFF"
		msg = OFF

	oscmsg.append(msg)

	try:
		client.send(oscmsg)
	except Exception as e:
		connected = False
	

if __name__ == "__main__":

	while not connected:
		try:
			client.connect((conf.HOST, conf.PORT))
			connected = True
		except Exception as e:
			continue

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIR_PIN, GPIO.IN)

	GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, on_transition_cb, bouncetime=1000)

	try:
		while True:
			if connected:
				time.sleep(3)
			else:
				print "connecting... " + HOST
				client.connect((conf.HOST, conf.PORT))
	except Exception as e:
		raise
	finally:
		print "cleaning up"
		GPIO.cleanup()

