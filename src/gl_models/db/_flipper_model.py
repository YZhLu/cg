from flipper_angles import FlipperAngles
from OpenGL import GL as gl
from .. import cube_model, block_model


def draw_arm_base(angles: FlipperAngles, texture_id: int, l=True):
    
    """Modelo do braço.
     Trata-se das sequências de matrizes que são enviadas
     ao OpenGL para desenhar o braço com textura.
    """

    if(l):
    #  origem posicionada no centro do braco
        gl.glTranslatef(5.5, 0.0, 4.0)
    #  os angulos da base e do ombro rotacionam o mesmo cubo, mas em eixos diferentes
    #gl.glRotatef(angles.base_in_degrees, 0.0, 1.0, 0.0)
        gl.glRotatef(angles.shoulder_in_degrees, 0.0, 1.0, 0.0)

        gl.glTranslatef(0.0, 0.0, -2.0)
        gl.glPushMatrix()
        gl.glScalef(0.4, 2.0, 3.0)
        gl.glColor3f(1.0, 1.0, 0.0)  # cyan color
        cube_model.draw_cube(1.0, texture_id)
    #block_model.draw(1, 1, 1, 1, 22, 0, 1, rotation_angle = 0, rotation_axis = [0, 0, 0])
    
    #block_model.draw(0.4, 2, 1, 0, 8, 0, 0, rotation_angle = 0, rotation_axis = [0, 0, 0])
        gl.glPopMatrix()
    
    else:
        gl.glTranslatef(0.0, 0.0, -6.0)
        gl.glRotatef(angles.shoulder_in_degrees, 0.0, 1.0, 0.0)

        gl.glTranslatef(0.0, 0.0, 2.0)
        gl.glPushMatrix()
        gl.glScalef(0.4, 2.0, 3.0)
        gl.glColor3f(0.0, 1.0, 1.0)  # cyan color
        cube_model.draw_cube(1.0, texture_id)
        gl.glPopMatrix()

    ''''
    #  origem posicionada no cotovelo
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glRotatef(angles.elbow_in_degrees, 0.0, 0.0, 1.0)
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glPushMatrix()
    gl.glScalef(2.0, 0.4, 1.0)
    gl.glColor3f(0.0, 1.0, 1.0)  # cyan color
    cube_model.draw_cube(1.0, texture_id)
    gl.glPopMatrix()

    '' '
    # o dedo de baixo garra
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glPushMatrix()
    gl.glTranslatef(0.0, -0.2, 0.0)
    gl.glRotatef(angles.bottom_claw_in_degrees, 0.0, 0.0, 1.0)
    gl.glTranslatef(0.25, 0.0, 0.0)
    gl.glScalef(0.5, 0.1, 0.33)
    gl.glColor3f(0.0, 1.0, 0.0)
    cube_model.draw_cube(1.0, texture_id)
    gl.glPopMatrix()

    # o dedo de cima garra
    gl.glTranslatef(0.0, 0.2, 0.0)
    gl.glPushMatrix()
    gl.glTranslatef(0.0, 0.0, 0.0)
    gl.glRotatef(angles.upper_claw_in_degrees, 0.0, 0.0, 1.0)
    gl.glTranslatef(0.25, 0.0, 0.0)
    gl.glScalef(0.5, 0.1, 0.33)
    gl.glColor3f(0.0, 1.0, 0.0) 
    cube_model.draw_cube(1.0, texture_id)
    gl.glPopMatrix()
    '''
