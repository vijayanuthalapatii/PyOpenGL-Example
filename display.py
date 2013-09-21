#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py
from __OpenGLInit__ import * #LOAD OpenGLInitialize() FROM FILE __OpenInit__.py

class Display(object):
	"""Display class to openGL window"""
	def __init__(self, screen_size, fullscreen=False, multisample=False, icon=None, fill_color=None):
		super(Display, self).__init__()
		self.screen_size = screen_size
		if icon == None:icon = pygame.Surface((1,1)); icon.set_alpha(0)
		pygame.display.set_icon(icon)
		self.multisample = multisample
		if self.multisample:pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 1)
		else:
			 pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 0)
		self.set_fullScreen(self.screen_size)
		if fill_color == None: self.screen_size.fill((200, 200, 200))
		OpenInitialize()

	def set_fullScreen(self, value):
		if value:
			self._screenFlags = OPENGL|DOUBLEBUF|FULLSCREEN; self.fullscreen = True
		else:self._screenFlags = OPENGL|DOUBLEBUF|FULLSCREEN; self.fullscreen = False
		pygame.display.set_mode(self.screen_size, self._screenFlags)

	def set_flip_option(self):
		return pygame.display.flip()

	def toggle_fullscreen_mode(self):
		self.fullscreen = not self.fullscreen
		return self.set_fullScreen(self.fullscreen)