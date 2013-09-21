#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py

pygame.init()

def shapeTexturing(boolean):
	if boolean: glEnable(GL_TEXTURE_2D)
	else: glDisable(GL_TEXTURE_2D)

def set_shapeTexturing(texture, filters=[], size="automatic"):
	pass