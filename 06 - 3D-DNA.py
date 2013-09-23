# Pygame/PyopenGL
#
# Keywords: Alpha Blending, Textures, Animation, Double Buffer

import random
import numpy
import Image
import sys
import time

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py
from display import Display
from viewPorts import *
from texture import Texture
from math import * # trigonometria

SCREEN_SIZE = [1024, 768]

class DNA:
  """Spiral form like an DNA with Animation"""
  def __init__(self):
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);    

    glLoadIdentity()
    gluPerspective(90,1,0.01,1000)
    gluLookAt(sin(t/500.0)*2,sin(t/500.0)*8,cos(t/200.0)*3,0,0,0,0,1,0)

    glMatrixMode(GL_MODELVIEW)

    texture=glGenTextures( 1 )

    glBindTexture( GL_TEXTURE_2D, texture );
    glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );

    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,  GL_REPEAT);
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,  GL_REPEAT );
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    pulse = 0

    texdata=[[[0.0,0,1,1],
              [0.0,99,0,0],
              [0.0,1,0,1],
              [0.0,0,0,0]],
             [[0.99,99,0,0],
              [pulse,pulse,pulse,1],
              [pulse,pulse,pulse,1],
              [0.0,0,0,0]],
             [[0.0,1,0,1],
              [1,pulse,pulse,1],
              [pulse,pulse,0,1],
              [0.0,0,0,0]],
             [[0.0,99,0,0],
              [0.0,0,0,0],
              [0.0,0,99,0],
              [0.0,0,0,0]]];

    glTexImage2Df(GL_TEXTURE_2D, 0,4,0,GL_RGBA,texdata)

    glEnable(GL_BLEND);
    glBlendFunc (GL_SRC_ALPHA, GL_ONE);
    glEnable(GL_DEPTH_TEST);
    glEnable( GL_TEXTURE_2D );
    glBindTexture( GL_TEXTURE_2D, texture );

    glBegin(GL_TRIANGLE_STRIP);

    for i in range(0,150):

        r=9.5
        d=1

        if (i%2==0):
            glTexCoord2f(0,i);
            glVertex3f( cos(i/r), -2.5+i*0.05, sin(i/r));
            # glVertex3f( cos(i/r)*pulse, -2.5+i*0.05, sin(i/r)*pulse);
        else:
            glTexCoord2f(1,i);
            glVertex3f( cos(i/r+3.14), -2.5+i*0.05+d, sin(i/r+3.14));
            # glVertex3f( cos(i/r+3.14)*pulse, -2.5+i*0.05+d+pulse*1, sin(i/r+3.14)*pulse);
    glEnd();
    glFlush();
    glDeleteTextures(texture);

if __name__ == '__main__':
	t=0
	display  = Display(SCREEN_SIZE)
	ViewPort3D((0,0, SCREEN_SIZE[0], SCREEN_SIZE[1]), 45).set_viewport()
	frames_per_second = pygame.time.Clock()

	while True:
		t=t+1
		DNA()
		time.sleep(0.009);
		display.get_events()
		display.set_flip_option()