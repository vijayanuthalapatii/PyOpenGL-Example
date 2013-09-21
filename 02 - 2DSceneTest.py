#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py
from display import Display
from viewPorts import *
pygame.init()

SCREEN_SIZE = [1024, 768]

window   = Display(SCREEN_SIZE)
_2D_view_= ViewPort2D((0,0, 1024, 768), 45)
_2D_view_.set_viewport()

while True:
	window.set_flip_option()
	window.get_events()