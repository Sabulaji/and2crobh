from robh import *


# dj("hand").dec()

# dj("ud").inc()


# class robh:
	# djs = [dj("hand"),dj("ud"),dj("lr")]

	# def w(self):
		# robh.djs[0].dec()


commands = {
    #"c":robh().c,
    # "loosen":robh().lossen,
    "w":robh().w,
    # "down":robh().down,
    # "left":robh().left,
    # "right":robh().right
}

#robh().w()

def run(command):
	print command
	try:
		commands[command]()
	except Exception,e:
		print "Oops",e



command = raw_input("run command:")
run(command)


