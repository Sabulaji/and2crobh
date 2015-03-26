#import RPi.GPIO as GPIO
from time import sleep

class dj:

	pins = {'hand':21,'ud':20,'lr':16}
	angles = {'hand':90,'ud':10,'lr':70}
	hz = 50
	pause_time = 0.05

	def __init__(self,name):
		self.name = name
		self.pin = dj.pins[self.name]
		self.angle = dj.angles[self.name]
		#GPIO.setmode(GPIO.BCM)
		#GPIO.setup(self.pin,GPIO.OUT)
		#GPIO.PWM(self.pin,dj.hz).start(self.angle2dutycycle(self.angle))
		print ("dj.init()")

	def inc(self):
		self.angle += 5
		#GPIO.PWM(self.pin,dj.hz).ChangeDutyCycle(self.angle2dutycycle(self.angle))
		sleep(dj.pause_time)
		print ("dj.inc()")

	def dec(self):
		self.angle -= 5
		#GPIO.PWM(self.pin,dj.hz).ChangeDutyCycle(self.angle2dutycycle(self.angle))
		sleep(dj.pause_time)
		self.angle2dutycycle(self.angle)
		print ("dj.dec()")

	def angle2dutycycle(self,angle):
		dutycycle = (angle * 11 + 500)/200.0
		print dutycycle
		return dutycycle
