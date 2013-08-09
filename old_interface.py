import urwid
import curses
import curses.wrapper
import os
import pdb
#import login as fblogin
#import feed as fbfeed



def main_window(screen):
	screen = curses.initscr()
	curses.start_color()
	(rows, cols) = screen.getmaxyx()
	screen.border(0)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
	screen.addstr(0, 0, "Facebook", curses.color_pair(4))
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
		elif c == ord('p'):
			toPost = post(screen)
			screen.addstr(rows/2, cols/2 - 20, toPost)
		elif c == ord('r'): screen.refresh()
		
def post(screen):
	try:
		cscrn = cdk.Screen(screen)
		entry = cdk.Mentry(cscrn, cdk.CENTER, cdk.CENTER, "Post to Timeline", "Text: ", 40, 3, 20, box=True)
		cscrn.refresh()
		#cscrn.keypad(0)
		string = entry.activate()
		if entry.getExitType() == cdk.vESCAPE_HIT:
			mesg = "Post cancelled."
			cdk.popup(cscrn, mesg)
			cscrn.destroy()
			return "Post cancelled."
		else if string != None: 
			return string
			cscrn.destroy()
		else:
			return "Something's wrong here."
	except:
		pass

curses.wrapper(main_window)
curses.endwin()
