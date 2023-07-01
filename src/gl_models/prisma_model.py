from OpenGL import GL as gl
import numpy as np

def draw(size: float, texture_id: int):
    
    n = [
        [0.0, -1.0, 0.0],   # 0
        [-1.0, 0.0, 0.0],   # 1
        [1.0, 0.0, -1.0],   # 2
        [0.0, 0.0, 1.0],    # 3
        [0.0, 1.0, 0.0]     # 4
    ]

    faces = [
        [0, 2, 1],     # 0
        [0, 3, 5, 2],  # 1
        [1, 2, 5, 4],  # 2
        [0, 1, 4, 3],  # 3
        [3, 4, 5],     # 4
    ]

    n = np.array(n)
    faces = np.array(faces, dtype=object)

    v = np.zeros(shape=(6, 3))
    
    #v[0][0] = v[0][1] = v[0][2] = v[1][1] = v[1][2] = v[2][0] = v[2][1] = v[3][0] = v[3][2] = v[4][2] = v[5][0] = 0
    v[1][0] = v[3][1] = v[4][0] = v[4][1] = v[5][1] = size
    v[2][2] = v[5][2] = -size

    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    for i in [4, 3, 2, 1, 0]:
        
        if (i != 0 and i != 4):
            gl.glBegin(gl.GL_QUADS)
            gl.glTexCoord2fv([0.0, 0.0])
            gl.glNormal3fv(n[i])  # 0

            gl.glTexCoord2fv([0.5, 0.0])
            gl.glVertex3fv(v[faces[i][0]])  # 1

            gl.glTexCoord2fv([1.0, 0.0])
            gl.glVertex3fv(v[faces[i][1]])  # 2

            gl.glTexCoord2fv([0.5, 0.0])
            gl.glVertex3fv(v[faces[i][2]])  # 4

            gl.glTexCoord2fv([1.0, 0.0])
            gl.glVertex3fv(v[faces[i][3]])  # 5

            gl.glEnd()
        else:
            gl.glBegin(gl.GL_TRIANGLES)
            gl.glTexCoord2fv([0.0, 0.0])
            gl.glNormal3fv(n[i])  # 0

            gl.glTexCoord2fv([0.5, 0.0])
            gl.glVertex3fv(v[faces[i][0]])  # 1

            gl.glTexCoord2fv([1.0, 0.0])
            gl.glVertex3fv(v[faces[i][1]])  # 2

            gl.glTexCoord2fv([0.5, 0.0])
            gl.glVertex3fv(v[faces[i][2]])  # 4

            gl.glEnd()