# Brownian motion -- an example of a NON multi-threaded Tkinter program ;)

from Tkinter import *
import random
import sys

WIDTH = 640
HEIGHT = 360
SIGMA = .2
BUZZ = 16
RADIUS = 6
LAMBDA = 10
FILL = 'blue'

stop = 0							# Set when main loop exits
root = None							# main window

def particle(canvas):				# particle = iterator over the moves
	r = RADIUS
	x = random.gauss(WIDTH/2.0, SIGMA)
	y = random.gauss(HEIGHT/2.0, SIGMA)
	p = canvas.create_rectangle(x-r, y-r, x+r, y+r, fill=FILL)
	while not stop:
		dx = random.gauss(0, BUZZ)
		dy = random.gauss(0, BUZZ)
		try:
			canvas.move(p, dx, dy)
		except TclError:
			break
		else:
			yield None

def move(particle): # move the particle at random time
	particle.next()
	dt = random.expovariate(LAMBDA)
	root.after(int(dt*1000), move, particle)

def main():
	global root, stop
	root = Tk()
	canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
	canvas.pack(fill='both', expand=1)
	np = 30
	if sys.argv[1:]:
		np = int(sys.argv[1])
	for i in range(np):				  # start the dance
		move(particle(canvas))
	try:
		root.mainloop()
	finally:
		stop = 1

if __name__ == '__main__':
	main()
