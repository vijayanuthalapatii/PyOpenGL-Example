#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py
from __OpenInit__ import * #LOAD OpenGLInitialize() FROM FILE __OpenInit__.py

class Display(object):
	"""Display class to openGL window"""
	def __init__(self, screen_size, fullscreen=False, multisample=False, icon=None):
		super(Display, self).__init__()
		self.screen_size = screen_size
		if icon == None:icon = pygame.Surface((1,1)); icon.set_alpha(0)
		pygame.display.set_icon(icon)
		self.multisample = multisample
		if self.multisample:pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 1)
		else:
			 pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 0)
		self.set_fullScreen(self.screen_size)
		self.clear_color = (0,0,0)
		OpenGLInitialize()

		