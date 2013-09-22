#--*-- coding:UTF-8 --*--

from __init__ import * #LOAD DEPENDENCIES FROM FILE __init__.py
from texture import *
from math import * # trigonometria

def init():
  glClearColor(0.0, 0.0, 0.0, 0.0);

def display():
  # clear all pixels
  glClear(GL_COLOR_BUFFER_BIT);

  # clear the modeling stack matrix
  glLoadIdentity();

  # set the observer
  gluLookAt(0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

  # draw a white
  glColor3f(1.0, 2.0, 1.0)
   
  # wireframed sphere
  glutWireSphere (2.0, 50, 10);
  glFlush();


def reshape(w,h):
  # set the viewpor dimensions 
  glViewport(0, 0, w, h); 
  
  #  set the viewing parameters 
  glMatrixMode(GL_PROJECTION);
  
  # clear the projection stack matrix 
  glLoadIdentity();
  glFrustum(-1.5, 1.5, -1.5, 1.5, 1.5, 20.0);
  
  # restore the modeling matrix mode
  glMatrixMode(GL_MODELVIEW);

name = 'wiresphere_glut'
def main():
  glutInit();
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
  glutInitWindowSize(530, 530); 
  glutInitWindowPosition (100, 100);
  glutCreateWindow(name);
  init()
  glutDisplayFunc(display);
  glutReshapeFunc(reshape);
  glutMainLoop();

if __name__ == '__main__':
  main()