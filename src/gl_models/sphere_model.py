from OpenGL import GL as gl
import numpy as np
import math

def draw(radius: float = 1.0, texture_id: int = 0, num_segments: int = 12, num_slices: int = 12):
    phi_step = 2 * math.pi / num_segments
    theta_step = math.pi / num_slices

    n = []
    v = []

    for i in range(num_slices + 1):
        theta = i * theta_step
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)

        for j in range(num_segments + 1):
            phi = j * phi_step
            sin_phi = math.sin(phi)
            cos_phi = math.cos(phi)

            x = radius * cos_phi * sin_theta
            y = radius * cos_theta
            z = radius * sin_phi * sin_theta

            v.append([x, y, z])
            n.append([x / radius, y / radius, z / radius])

    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    for i in range(num_slices):
        gl.glBegin(gl.GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            vertex_index = i * (num_segments + 1) + j
            gl.glNormal3fv(n[vertex_index])
            gl.glTexCoord2fv([j / num_segments, i / num_slices])
            gl.glVertex3fv(v[vertex_index])

            next_vertex_index = (i + 1) * (num_segments + 1) + j
            gl.glNormal3fv(n[next_vertex_index])
            gl.glTexCoord2fv([j / num_segments, (i + 1) / num_slices])
            gl.glVertex3fv(v[next_vertex_index])
        gl.glEnd()
