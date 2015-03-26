import RPi.GPIO as GPIO
import time



"""
	0: 0.5/20=2.5% 
	180: 2.5/20=12.5% 
	90: 1.5/20=7.5% 
	
	dutycycle = (angle * 11 + 500)/200

"""