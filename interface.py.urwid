import urwid

def exit_on_q(key):
	if key in ('q', 'Q'):
		raise urwid.ExitMainLoop()
		
palette = [
	('bg', 'white', 'black'),]
	
bottom = urwid.Text(('bg', u"Post	Reload"), align='left')
map1 = urwid.AttrMap(bottom, 'bg')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()
