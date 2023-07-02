from gl_models import cilinder_model
from OpenGL import GL as gl

def draw(size: list = [1,1,1], pos: list = [0,0,0], color: list = [255, 255, 255], texture_id: int = 0, rangle: float = 0, raxis: list = [0, 0, 0]):
    gl.glPushMatrix()
    #  origem posicionada no centro da peça
    gl.glTranslatef(pos[0], pos[1], pos[2])
    #  os angulos e eixos de rotação
    gl.glRotatef(rangle, raxis[0], raxis[1], raxis[2])
    # size
    gl.glScalef(size[0], size[1], size[2])
    # cor
    gl.glColor3f(color[0], color[1], color[2])
    # base & texture
    cilinder_model.draw(color[0], color[1], color[2], texture_id)
    gl.glPopMatrix()
    