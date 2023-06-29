from gl_models import block_model

def draw():
    block_model.draw_cube(width = 0.3, height = 2, depth = 18, texture_id = 2, new_x = -18, new_y = 0, new_z = 0, rotation_angle = 0, rotation_axis = [0, 0, 0])
    block_model.draw_cube(0.3, 2, 6, 2, 8, 0, 0, rotation_angle = 0, rotation_axis = [0, 0, 0])
    block_model.draw_cube(18, 2, 0.3, 0, -9, 0, -9, rotation_angle = 0, rotation_axis = [0, 0, 0])
    block_model.draw_cube(18, 2, 0.3, 0, -9, 0, 9, rotation_angle = 0, rotation_axis = [0, 0, 0])
    block_model.draw_cube(0.2, 2, 8, 0, 2.8, 0, -6.2, rotation_angle=45, rotation_axis=[0, 1, 0])
    block_model.draw_cube(0.2, 2, 8, 0, 2.8, 0, 6.2, rotation_angle=-45, rotation_axis=[0, 1, 0])