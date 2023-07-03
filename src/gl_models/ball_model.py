from gl_models import sphere_model
from OpenGL import GL as gl
from ball_position import BallPosition

def draw(ball_pos: BallPosition, size: list = [1,1,1], color: list = [1.0, 1.0, 1.0], texture_id: int = 0, rangle: float = 0, raxis: list = [0, 0, 0]):
    gl.glPushMatrix()
    #  origem posicionada no centro da peça
    gl.glTranslatef(ball_pos.sphere_position[0], ball_pos.sphere_position[1], ball_pos.sphere_position[2])
    #  os angulos e eixos de rotação
    gl.glRotatef(rangle, raxis[0], raxis[1], raxis[2])
    # size
    gl.glScalef(size[0], size[1], size[2])
    # cor
    gl.glColor3f(color[0], color[1], color[2])
    # base & texture
    sphere_model.draw(texture_id=texture_id)
    gl.glPopMatrix()