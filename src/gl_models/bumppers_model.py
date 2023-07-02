from gl_models import bumpper_model
from OpenGL import GL as gl


def draw():
    bumpper_model.draw(size = [0.75, 2, 0.75], pos = [-2,0,0], color=[255, 0, 0])
    bumpper_model.draw(pos = [-15,0,0], size = [0.5, 2, 0.5])
    #bumpper_model.draw(size = [0.3, 2, 6], pos = [8, 0, 0])
    bumpper_model.draw(pos = [-12, 0, -6], color = [255, 0, 255], size = [0.75, 2, 0.75])
    bumpper_model.draw(pos = [-12, 0, 6], color = [255, 0, 255], size = [0.75, 2, 0.75])
    bumpper_model.draw(pos = [-9, 0, 2], color = [0, 0, 0], size = [0.75, 2, 1.0])
    bumpper_model.draw(pos = [-9, 0, -2], color = [0, 0, 0], size = [1.0, 2, 0.75])
    bumpper_model.draw(pos = [-5, 0, -4.5], color = [255, 0, 255], size = [0.75, 2, 0.75])
    bumpper_model.draw(pos = [-5, 0, 4.5], color = [255, 0, 255], size = [0.75, 2, 0.75])
    bumpper_model.draw(size = [0.2, 2, 1.25], pos = [-1.8, 0, -5.8], rangle = 45, raxis = [0, 1, 0])
    bumpper_model.draw(size = [0.2, 2, 1.25], pos = [-1.8, 0, 5.8], rangle = -45, raxis = [0, 1, 0])
    bumpper_model.draw(pos = [2.0, 0, 3.0], color = [0, 255, 255])
    bumpper_model.draw(pos = [2.0, 0, -3.0], color = [255, 255, 0])
    