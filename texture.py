#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py

pygame.init()

def shapeTexturing(boolean):
	if boolean: glEnable(GL_TEXTURE_2D)
	else: glDisable(GL_TEXTURE_2D)

def set_shapeTexturing(texture, filters=[], size="automatic"):
	pass

class Texture(object):
	"""designed for 32 bit png images (with alpha channel)"""
	def __init__(self, filename):
		super(Texture, self).__init__()
		self.texID = 0
		self.LoadTexture(filename)
	def LoadTexture(self, filename):
		try:
			textureSurface = pygame.image.load(filename)
			textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
			self.texID  = glGenTextures(1)

			glBindTexture(GL_TEXTURE_2D, self.texID)
			glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(),	0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
			glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
			glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
		except Exception, e:
			print "textura: %s não pode ser aberta ou encontrada."%(filename)

	def __del__(self):
		glDeleteTextures(self.texID)
		