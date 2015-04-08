#rom dj import *
import RPi.GPIO as GPIO
from time import sleep

class gpiooutput:

	pins = [21,20,16]
	#      21      ||      20      ||      16
	###############################################
	#  001 ||  010 || 011  || 100  || 101  || 110
	#lr.inc||lr.dec||ud.dec||ud.inc||cl.inc||cl.dec
	pause_time = 0.1

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		for i in gpiooutput.pins:
			GPIO.setup(i,GPIO.OUT)
		self.resetto0()

	def setHigh(self,i):
		GPIO.output(int(i),GPIO.HIGH)
		#print(i , "HIGH")

	def setLow(self,i):
		GPIO.output(int(i),GPIO.LOW)
		#print(i , "LOW")

	def resetto0(self):
		for i in gpiooutput.pins:
			self.setLow(i)

	def w(self):
		#robh.djs[1].dec()
		#print ("robh.w()")
		self.setLow(gpiooutput.pins[0])
		self.setHigh(gpiooutput.pins[1])
		self.setHigh(gpiooutput.pins[2])
		sleep(gpiooutput.pause_time)
		self.resetto0()

	def s(self):
		#robh.djs[1].inc()
		self.setHigh(gpiooutput.pins[0])
		self.setLow(gpiooutput.pins[1])
		self.setLow(gpiooutput.pins[2])
		sleep(gpiooutput.pause_time)
		self.resetto0()

	def a(self):
		#robh.djs[2].inc()
		self.setLow(gpiooutput.pins[0])
		self.setLow(gpiooutput.pins[1])
		self.setHigh(gpiooutput.pins[2])
		sleep(gpiooutput.pause_time)
		self.resetto0()

	def d(self):
		#robh.djs[2].dec()
		self.setLow(gpiooutput.pins[0])
		self.setHigh(gpiooutput.pins[1])
		self.setLow(gpiooutput.pins[2])
		sleep(gpiooutput.pause_time)
		self.resetto0()

	def c(self):
		#robh.djs[0].inc()
		self.setHigh(gpiooutput.pins[0])
		self.setLow(gpiooutput.pins[1])
		self.setHigh(gpiooutput.pins[2])
		sleep(gpiooutput.pause_time)
		self.resetto0()

	def l(self):
		#robh.djs[0].dec()
		self.setHigh(gpiooutput.pins[0])
		self.setHigh(gpiooutput.pins[1])
		self.setLow(gpiooutput.pins[2])
		sleep(gpiooutput.pause_time)
		self.resetto0()
