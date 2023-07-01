from gl_models import block_model

def draw():
    block_model.draw(size = [0.3, 2, 18], pos = [-18,0,0])
    block_model.draw(size = [0.3, 2, 6], pos = [8, 0, 0])
    block_model.draw(size = [18, 2, 0.3], pos = [-9, 0, -9])
    block_model.draw(size = [18, 2, 0.3], pos = [-9, 0, 9])
    block_model.draw(size = [0.2, 2, 8], pos = [2.8, 0, -6.2], rangle = 45, raxis = [0, 1, 0])
    block_model.draw(size = [0.2, 2, 8], pos = [2.8, 0, 6.2], rangle = -45, raxis = [0, 1, 0])
    