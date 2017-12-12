#!/usr/bin/env python3
import curses
import time
import random

random.seed(1)

class text:
	def __init__(self,text,x,y):
		self.text=text
		self.x=x
		self.y=y

def run():
	screen=curses.initscr()
	screen.nodelay(1)
	curses.start_color()
	curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
	#curses.init_pair(2,curses.COLOR_ORANGE,curses.COLOR_BLACK)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
	curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_BLACK)
	curses.init_pair(5,curses.COLOR_BLUE,curses.COLOR_BLACK)
	#curses.init_pair(6,curses.COLOR_PURPLE,curses.COLOR_BLACK)
	q=-1
	vert=1
	horiz=1
	color=1
	b=curses.A_BOLD
	r=curses.A_REVERSE
	t=text("JORDAN",0,0)
	texts=["JORDAN","BATMAN","PYTHON","GOLANG","COFFEE"]
	change=False
	while q!=ord(' '):
		dims=screen.getmaxyx()
		screen.clear()
		t.y+=vert
		t.x+=horiz
		if t.y==screen.getmaxyx()[0]-1:
			vert = -1
			change=True
		elif t.y==0:
			vert = 1
			change=True
		if t.x==screen.getmaxyx()[1]-len(t.text)-1:
			horiz = -1
			change=True
		elif t.x==0:
			horiz = 1
			change=True
		if change:
			t.text=random.choice(texts)
			change=False
		if(color<5):
			color+=1
		else:
			color=1
		screen.addstr(t.y,t.x,t.text,curses.color_pair(color)|r)
		screen.refresh()
		time.sleep(0.09)
		q=screen.getch()
	curses.endwin()

try:
	curses.wrapper(run())
except:
	pass
