""" from OpenGL import GL as gl
import numpy as np
import math

def draw(radius: float, height: float, texture_id: int, num_segments: int = 50):
    angle_step = 2 * math.pi / num_segments

    n = [
        [0.0, 1.0, 0.0],  # Topo
        [0.0, -1.0, 0.0],  # Base
    ]

    v = np.zeros(shape=(2 * num_segments, 3))
    for i in range(num_segments):
        angle = i * angle_step
        v[i][0] = radius * math.cos(angle)
        v[i][1] = height / 2
        v[i][2] = radius * math.sin(angle)
        v[i + num_segments][0] = radius * math.cos(angle)
        v[i + num_segments][1] = -height / 2
        v[i + num_segments][2] = radius * math.sin(angle)

    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    for i in range(num_segments):
        gl.glBegin(gl.GL_QUADS)

        # Lateral
        gl.glNormal3fv([math.cos(angle), 0.0, math.sin(angle)])
        gl.glTexCoord2fv([0.0, 0.0])
        gl.glVertex3fv(v[i])
        gl.glTexCoord2fv([1.0, 0.0])
        gl.glVertex3fv(v[(i + 1) % num_segments])
        gl.glTexCoord2fv([1.0, 1.0])
        gl.glVertex3fv(v[(i + 1) % num_segments + num_segments])
        gl.glTexCoord2fv([0.0, 1.0])
        gl.glVertex3fv(v[i + num_segments])

        gl.glEnd()

    # Topo
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glNormal3fv(n[0])
    gl.glTexCoord2fv([0.5, 0.5])
    gl.glVertex3fv([0.0, height / 2, 0.0])
    for i in range(num_segments):
        angle = i * angle_step
        gl.glNormal3fv(n[0])
        gl.glTexCoord2fv([0.5 + 0.5 * math.cos(angle), 0.5 + 0.5 * math.sin(angle)])
        gl.glVertex3fv([radius * math.cos(angle), height / 2, radius * math.sin(angle)])
    gl.glEnd()

    # Base
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glNormal3fv(n[1])
    gl.glTexCoord2fv([0.5, 0.5])
    gl.glVertex3fv([0.0, -height / 2, 0.0])
    for i in range(num_segments):
        angle = i * angle_step
        gl.glNormal3fv(n[1])
        gl.glTexCoord2fv([0.5 + 0.5 * math.cos(angle), 0.5 + 0.5 * math.sin(angle)])
        gl.glVertex3fv([radius * math.cos(angle), -height / 2, radius * math.sin(angle)])
    gl.glEnd()
 """
from OpenGL import GL as gl
import numpy as np
import math

def draw(R, G, B, texture_id):
    radius = 1
    height = 1
    x = 0.0
    z = 0.0
    angle = 0.0
    angle_stepsize = 0.1
    num_segments = 2*math.pi * angle_stepsize


    n = [
        [0.0, 1.0, 0.0],  # Topo
        [0.0, -1.0, 0.0],  # Base
    ]

    # v = np.zeros(shape=(2 * int(num_segments), 3))
    # for i in range(int(num_segments)):
    #     angle = i * angle_stepsize
    #     v[i][0] = radius * math.cos(angle)
    #     v[i][1] = height
    #     v[i][2] = radius * math.sin(angle)
    #     v[i + num_segments][0] = radius * math.cos(angle)
    #     v[i + num_segments][1] = -height
    #     v[i + num_segments][2] = radius * math.sin(angle)
    
    # gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
    # gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    # 
    # 
    # Draw the tube
    #gl.glColor3ub(R-40, G-40, B-40)
    gl.glColor3f(1,1.0,0.54)
    gl.glBegin(gl.GL_QUAD_STRIP)
    angle = 0.0
    while angle < 2 * math.pi:
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        gl.glVertex3f(x, height, z)
        gl.glVertex3f(x, 0.0, z)
        angle += angle_stepsize
    gl.glVertex3f(radius, height, 0.0)
    gl.glVertex3f(radius, 0.0, 0.0)
    gl.glEnd()

    # Draw the circle on top of the cylinder
    gl.glColor3ub(R, G, B)
    gl.glBegin(gl.GL_POLYGON)
    angle = 0.0
    while angle < 2 * math.pi:
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        gl.glVertex3f(x, height, z)
        angle += angle_stepsize
    gl.glVertex3f(radius, height, 0.0)
    gl.glEnd()
    
    # Draw the circle on bottom of the cylinder
    #gl.glColor3ub(R, G, B)
    gl.glBegin(gl.GL_POLYGON)
    angle = 0.0
    while angle < 2 * math.pi:
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        gl.glVertex3f(x, 0.0, z)
        angle += angle_stepsize
    gl.glVertex3f(radius, 0.0, 0.0)
    gl.glEnd()