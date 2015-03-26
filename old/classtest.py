
'''
class dj:
	pins = {'hand':21,'ud':20,'lr':16}
	angles = {'hand':90,'ud':10,'lr':70}
	hz = 50
	pause_time = 0.05

	def __init__(self,name):
		self.name = name
		self.pin = dj.pins[self.name]
		self.angle = dj.angles[self.name]
		print "dj-inited"

	def a2d(self,angle):
		dutycycle = (angle * 11 + 500)/200.0
		print dutycycle
		return dutycycle

	def inc(self):
		self.angle += 5
		print self.angle
		self.a2d(self.angle)
		print "dj-inc"

	def dec(self):
		self.angle -= 5		
		print self.angle
		self.a2d(self.angle)
		print "dj-dec"

class robh:
	djs = [dj("hand"),dj("ud"),dj("lr")]

	def w(self):
		robh.djs[1].dec()
		print "w"

	def s(self):
		robh.djs[1].inc()
		print "s"

	def a(self):
		robh.djs[2].inc()
		print "a"

	def d(self):
		robh.djs[2].dec()
		print "d"

	def c(self):
		robh.djs[0].inc()
		print "c"

	def l(slef):
		robh.djs[0].dec()
		print "l"

commands = {
    "c":robh.c,
    "l":robh.l,
    "w":robh.w,
    "s":robh.s,
    "a":robh.a,
    "d":robh.d
}

def execute(command):
	print command
	commands[command]()

while True:
	command = raw_input("command:")

	try:
		execute(command)
	except Exception,e:
		print "Oops,try again"
'''

class a:
	def __init__(self,name):
		self.name = name
		print self.name

	def b(self):
		print "this is a.b()"

test = a(yo)
test.b()





