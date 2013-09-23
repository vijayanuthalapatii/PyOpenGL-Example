#--*-- coding:UTF-8 --*--
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT

import pygame, sys, os, math, random, time, numpy

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from OpenGL.GLU import gluLookAt #THIS LINE DOESN'T MAKE ANY SENSE WITH THE ABOVE LINE.

from os.path import sep
from sys import exit

from math import *
from ctypes import *

from texture import Texture

SCREEN_SIZE = [1024, 768]

def OpenInitialize():
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glShadeModel(GL_SMOOTH)
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClearDepth(1.0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_ALPHA_TEST)
	glDepthFunc(GL_LEQUAL)
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
	glAlphaFunc(GL_NOTEQUAL,0.0)


class Display(object):
	"""Display class to open an openGL window"""
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
		#if fill_color == None: pygame.Surface.fill((200, 200, 200))
		OpenInitialize()

	def set_fullScreen(self, value):
		if value:
			self._screenFlags = OPENGL|DOUBLEBUF|FULLSCREEN; self.fullscreen = True
		else:self._screenFlags = OPENGL|DOUBLEBUF|FULLSCREEN; self.fullscreen = False
		self.show_screen= pygame.display.set_mode(self.screen_size, self._screenFlags)
		return self.show_screen

	def set_flip_option(self):
		return pygame.display.flip()

	def toggle_fullscreen_mode(self):
		self.fullscreen = not self.fullscreen
		return self.set_fullScreen(self.fullscreen)

	def get_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					exit()
				if event.key == K_f:
					self.fullscreen = not self.fullscreen
					if self.fullscreen:
						pygame.display.set_mode(self.screen_size, FULLSCREEN, 32)
					else:	pygame.display.set_mode(self.screen_size, 0, 32)

class MiniDroidTest:
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

class Quads(object):
	"""Obejto Geometrico"""
	def __init__(self, rectstyle, color, width=0, alpha=255.0):
		self.px, self.py, self.w, self.h = rectstyle
		self.color = color

		self.points = [[self.px, self.y], [self.x+self.w, self.y], [self.x+self.w, self.y+self.h], [self.x, self.y+self.h]]
    points = flip_points(points)
    offset = window.get_size()[1]
    if not width:
        polygon(points, color, aa=False, alpha=alpha)
    else:
        lines(points, color, width=width, aa=False, alpha=alpha, closed=1)

		

if __name__ == '__main__': 
	pygame.init()

	window   = Display(SCREEN_SIZE)

	frames_per_second = pygame.time.Clock()
	droid = MiniDroidTest()
	droid.resize((SCREEN_SIZE[0], SCREEN_SIZE[1]))
	while True:
		window.get_events()
		droid.Input()
		droid.draw()
		window.set_flip_option()
		frames_per_second.tick(70)