from dj import *

class robh:
	djs = [dj("hand"),dj("ud"),dj("lr")]

	def w(self):
		robh.djs[1].dec()
		print ("robh.w()")

	def s(self):
		robh.djs[1].inc()

	def a(self):
		robh.djs[2].inc()

	def d(self):
		robh.djs[2].dec()

	def c(self):
		robh.djs[0].inc()

	def l(self):
		robh.djs[0].dec()