#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py

#On this file we can create our viewport to Genereate OpenGl view

def init2d(rect, prox, far):
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glDisable(GL_LIGHTING)
	glEnable(GL_TEXTURE_2D)
	glViewport(*rect)
	glMatrixMode(GL_PROJECTION)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glOrtho(rect[0],rect[2],rect[1],rect[3],prox,far)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
def init3d(rect, angle, prox, far):
	glViewport(*rect)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(angle,float(rect[2])/float(rect[3]),prox,far)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

class ViewPort2D(object):
	"""OpenViewPort2D"""
	def __init__(self, rect, prox=-10, far=10.0):
		super(ViewPort2D, self).__init__()
		self._rect = rect
		self._prox = prox
		self._far  = far
	def set_near(self, value):
		self._prox = value
	def set_far(self, value):
		self._far = value
	def set_viewport(self):
		init2d(self._rect, self._prox, self._far)


class ViewPort3D(object):
	"""OpenViewPort3D"""
	def __init__(self, rect, angle, prox=0.1, far=1000.0):
		super(ViewPort3D, self).__init__()
		self._rect = rect
		self._angle= angle
		self._prox = prox
		self._far  = far
	def set_angle(self, value):
		self._angle = value
	def set_near(self, value):
		self._prox  = value
	def set_far(self, value):
		self._far = value
	def set_viewport(self):
		init3d(self._rect, self._angle, self._prox, self._far)