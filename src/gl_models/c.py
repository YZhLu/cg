from OpenGL import GL as gl
import numpy as np

def draw(size: float, texture_id: int):

    gl.glBegin(gl.GL_QUADS)
    gl.glVertex3f(0.5, 0, 0.5)
    gl.glVertex3f(0.5, 0, -0.5)
    gl.glVertex3f(-0.5, 0, -0.5)
    gl.glVertex3f(-0.5, 0, 0.5)

    gl.glVertex3f(0.5,0,-0.5)
    gl.glVertex3f(0.5,1,-0.5)
    gl.glVertex3f(-0.5,1,-0.5)
    gl.glVertex3f(-0.5,0,-0.5)

    gl.glVertex3f(0.5,1,-0.5)
    gl.glVertex3f(-0.5,1,-0.5)
    gl.glVertex3f(-0.5,0,0.5)
    gl.glVertex3f(0.5,0,0.5)
    gl.glEnd()
    
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex3f(0.5,0,0.5)
    gl.glVertex3f(0.5,1,-0.5)
    gl.glVertex3f(0.5,0,-0.5)

    gl.glVertex3f(-0.5,0,0.5)
    gl.glVertex3f(-0.5,1,-0.5)
    gl.glVertex3f(-0.5,0,-0.5)
    gl.glEnd()

