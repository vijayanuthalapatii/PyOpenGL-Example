#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py
from display import Display
from viewPorts import *
from texture import Texture

SCREEN_SIZE = [1024, 768]

class Main():
	def __init__(self):
		self.textura = Texture(os.path.join("images","minidroid.png")) #It also Work with the nerd - mike.png
		self.x , self.y = 0.0 , 0.0

	# Resize the image to draw on the screen
	def resize(self,(width, height)):
		if height==0:
			height=1
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(-8.0, 8.0, -6.0, 6.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	#Draw minidroid on the screen	
	def draw(self):
		#Without these lines below the image will not buffer and cache to memory
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glDisable(GL_LIGHTING)
		glEnable(GL_TEXTURE_2D)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		glPushMatrix()

		glTranslatef(self.x, self.y, 0.0)
		glColor4f(1.5, 1.0, 1.0,1.0)
		glBindTexture(GL_TEXTURE_2D,self.textura.texID)
		glBegin(GL_QUADS)
		
		glTexCoord2f(0.0,1.0)
		glVertex2f(-1.0, 4.0)
		
		glTexCoord2f(1.0,1.0)
		glVertex2f(3.0, 3.0)
		
		glTexCoord2f(1.0,0.0)
		glVertex2f(3.0, -4.0)
		
		glTexCoord2f(0.0,0.0)
		glVertex2f(-1.0, -4.0)
		
		glEnd()
		
		glPopMatrix()
	
	# This Input Method gets_events from the keyboard	using pygame event
	def Input(self):
		key_event = pygame.key.get_pressed()
		if key_event[K_UP]:
			self.y+=0.1
		if key_event[K_DOWN]:
			self.y-=0.1
		
		if key_event[K_RIGHT]:
			self.x+=0.1
		if key_event[K_LEFT]:
			self.x-=0.1

if __name__ == '__main__': 
	pygame.init()

	window   = Display(SCREEN_SIZE)
	ViewPort2D((0,0, SCREEN_SIZE[0], SCREEN_SIZE[1]), 45).set_viewport()

	frames_per_second = pygame.time.Clock()
	droid = Main()
	droid.resize((SCREEN_SIZE[0], SCREEN_SIZE[1]))
	while True:
		window.get_events()
		droid.Input()
		droid.draw()
		window.set_flip_option()
		frames_per_second.tick(70)