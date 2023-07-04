from flipper_angles import FlipperAngles
from OpenGL import GL as gl
from . import prisma_model, block_model


def draw(angles: FlipperAngles, texture_id: int, l=True):
    
    """Modelo do flipper.
     Trata-se das sequências de matrizes que são enviadas
     ao OpenGL para desenhar o flipper com textura.
    """

    if(l):
        gl.glPushMatrix()
        gl.glTranslatef(5.6, 0.0, 3.2)
        gl.glRotatef(-45, 0.0, 1.0, 0.0)
        gl.glRotatef(angles.left_flipper_in_degrees, 0.0, 1.0, 0.0)
        gl.glScalef(0.4, 2.0, 2.5)
        gl.glColor3f(1.0, 1.0, 0.0)  # cyan color
        prisma_model.draw(1.0, texture_id)
        gl.glPopMatrix()
    
    else:
        gl.glPushMatrix()
        gl.glRotatef(180, 1, 0, 0)
        gl.glTranslatef(5.6, -2.0, 3.2)
        gl.glRotatef(-45, 0.0, 1.0, 0.0)
        gl.glRotatef(angles.right_flipper_in_degrees, 0.0, 1.0, 0.0)
        gl.glScalef(0.4, 2.0, 2.5)
        gl.glColor3f(0.0, 1.0, 1.0)  # cyan color
        prisma_model.draw(1.0, texture_id)
        gl.glPopMatrix()
       
