import curses
import curses.textpad
import os
#import login as fblogin
#import feed as fbfeed

stdscr = curses.initscr()
(rows, cols) = stdscr.getmaxyx()

def main_window(screen):
	screen.border(0)
	screen.addstr(0, 0, "Facebook")
	screen.addstr(rows-2, 2, "P", curses.A_BOLD)
	screen.addstr("ost")
	screen.addstr(rows-2, 10, "R", curses.A_BOLD)
	screen.addstr("eload")
	screen.addstr(rows-2, cols-6, "Q", curses.A_BOLD)
	screen.addstr("uit")
	screen.refresh()
	screen.leaveok(0)
	while 1:
		screen.move(rows-1,cols-1)
		c = screen.getch()
		if c == ord('q'): break
		elif c == ord('p'): post(screen)
		
def post(screen):
	postwin = curses.newwin(5, 40, rows/2 - 2, cols/2 - 20)
	curses.textpad.rectangle(postwin, 0, 0, 3, 39)
	box = curses.textpad.Textbox(postwin)
	(y, x) = postwin.getyx()
	postwin.move(y - 2, x)
	string = box.edit()
	postwin.clear()
	postwin.refresh()
	return

curses.wrapper(main_window)
