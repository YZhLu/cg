from OpenGL import GL as gl
import numpy as np

def draw(width: float, height: float, depth: float, texture_id: int, new_x: float, new_y: float, new_z: float, rotation_angle: float, rotation_axis: list):
    """
    Algoritmo tirado do próprio freeGlut: https://github.com/markkilgard/glut/blob/master/lib/glut/glut_shapes.c#L171
    sendo que foi adicionado textura no cubo
    """

    n = [
        [-1.0, 0.0, 0.0],  # 0
        [0.0, 1.0, 0.0],   # 1
        [1.0, 0.0, 0.0],   # 2
        [0.0, -1.0, 0.0],  # 3
        [0.0, 0.0, 1.0],   # 4
        [0.0, 0.0, -1.0],  # 5
    ]

    faces = [
        [0, 1, 2, 3],  # 0
        [3, 2, 6, 7],  # 1
        [7, 6, 5, 4],  # 2
        [4, 5, 1, 0],  # 3
        [5, 6, 2, 1],
        [7, 4, 0, 3]
    ]

    n = np.array(n)
    faces = np.array(faces)

    v = np.zeros(shape=(8, 3))
    v[0][0] = v[1][0] = v[2][0] = v[3][0] = -width / 2
    v[4][0] = v[5][0] = v[6][0] = v[7][0] = width / 2
    v[0][1] = v[1][1] = v[4][1] = v[5][1] = -height / 2
    v[2][1] = v[3][1] = v[6][1] = v[7][1] = height / 2
    v[0][2] = v[3][2] = v[4][2] = v[7][2] = -depth / 2
    v[1][2] = v[2][2] = v[5][2] = v[6][2] = depth / 2

    # Aplicar translação para nova posição
    translation_matrix = np.array([new_x, new_y, new_z])
    v += translation_matrix

    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    # Aplicar rotação
    gl.glPushMatrix()
    gl.glTranslatef(new_x, new_y, new_z)
    gl.glRotatef(rotation_angle, *rotation_axis)
    gl.glTranslatef(-new_x, -new_y, -new_z)

    for i in [5, 4, 3, 2, 1, 0]:
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

    gl.glPopMatrix()
