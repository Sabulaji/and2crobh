import RPi.GPIO as GPIO
from time import sleep

import pygame,sys
from pygame.locals import *

"""
def angle2dutycycle(angle):
	dutycycle = (angle * 11 + 500)/200.0
	print dutycycle
	return dutycycle
#angle to duty cycle

pause_time = 0.05

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

p = GPIO.PWM(21,50)

p.start(angle2dutycycle(90))

try:
	while 1:
		angle = raw_input("angle:")
		p.ChangeDutyCycle(angle2dutycycle(int(angle)))
		sleep(pause_time)

except KeyboardInterrupt:
	pass
p.stop()
GPIO.cleanup()
"""

def angle2dutycycle(angle):
	dutycycle = (angle * 11 + 500)/200.0
	print dutycycle
	return dutycycle
#angle to duty cycle

def clip():
	angle[0] = angle[0] + 10
	hand.ChangeDutyCycle(angle2dutycycle(angle[0]))
	print angle[0]
	sleep(pause_time)

def loose():
	angle[0] = angle[0] - 10
	hand.ChangeDutyCycle(angle2dutycycle(angle[0]))
	print angle[0]
	sleep(pause_time)

def up():
	angle[1] = angle[1] - 10
	ud.ChangeDutyCycle(angle2dutycycle(angle[1]))
	print angle[1]
	sleep(pause_time)

def down():
	angle[1] = angle[1] + 10
	ud.ChangeDutyCycle(angle2dutycycle(angle[1]))
	print angle[1]
	sleep(pause_time)


def left():
	angle[2] = angle[2] + 10
	lr.ChangeDutyCycle(angle2dutycycle(angle[2]))
	print angle[2]
	sleep(pause_time)

def right():
	angle[2] = angle[2] - 10
	lr.ChangeDutyCycle(angle2dutycycle(angle[2]))
	print angle[2]
	sleep(pause_time)


pause_time = 0.05

hz = 50

pin = [21,20,16]

angle = [90,10,90]

pin[0] = raw_input("Hand's pin:")
pin[1] = raw_input("UD's pin:")
pin[2] = raw_input("LR's pin:")

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(pin[0]),GPIO.OUT)
GPIO.setup(int(pin[1]),GPIO.OUT)
GPIO.setup(int(pin[2]),GPIO.OUT)

hand = GPIO.PWM(int(pin[0]),hz)
ud = GPIO.PWM(int(pin[1]),hz)
lr = GPIO.PWM(int(pin[2]),hz)

hand.start(angle2dutycycle(angle[0]))#90-135
ud.start(angle2dutycycle(angle[1]))
lr.start(angle2dutycycle(angle[2]))
sleep(pause_time)

#pygame.init()

try:
	while 1:
		# angle = raw_input("angle:")
		# p.ChangeDutyCycle(angle2dutycycle(int(angle)))
		# sleep(pause_time)
		# for event in pygame.event.get():

		# 	if event.type == KEYDOWN:

		# 		if event.key == K_LEFT:
		# 			left()
		# 		if event.key == K_RIGHT:
		# 			right()
		# 		elif event.key == K_UP:
		# 			up()
		# 		elif event.key == K_DOWN:
		# 			down()

		#pressed_keys = pygame.key.get_pressed()

		key = raw_input(">")

		if key == "a" :
			print left
			left()
		if key == "d" :
			print right
			right()
		if key == "w" :
			print up
			up()
		if key == "s" :
			print down
			down()

except KeyboardInterrupt:
	pass
hand.stop()
ud.stop()
lr.stop()
GPIO.cleanup()
