from camera import Camera
from OpenGL import GLUT as glut
from flipper_angles import FlipperAngles

class KeyboardController:
    __arm_angles: FlipperAngles
    __cam: Camera
    __theta_xz = 0
    __left_animation_frame = 0
    __right_animation_frame = 0
    __animation_duration = 60

    def __init__(self, arm: FlipperAngles, cam: Camera) -> None:
        self.__arm_angles = arm
        self.__cam = cam

    def key_press(self, key: bytes) -> None:
        match key.decode():
            case 'q':
                if self.__left_animation_frame == 0:
                    self.__left_animation_frame = 1
            case 'p':
                if self.__right_animation_frame == 0:
                    self.__right_animation_frame = 1


    def update_animation(self) -> None:
        if self.__left_animation_frame > 0:
            if self.__left_animation_frame <= self.__animation_duration // 2:
                angle = 90 * (self.__left_animation_frame / (self.__animation_duration // 2))
            else:
                angle = 90 * (1 - ((self.__left_animation_frame - (self.__animation_duration // 2)) / (self.__animation_duration // 2)))

            self.__arm_angles.left_flipper_in_degrees = angle

            self.__left_animation_frame += 1

            if self.__left_animation_frame > self.__animation_duration:
                self.__left_animation_frame = 0

            glut.glutPostRedisplay()

        if self.__right_animation_frame > 0:
            if self.__right_animation_frame <= self.__animation_duration // 2:
                angle = 90 * (self.__right_animation_frame / (self.__animation_duration // 2))
            else:
                angle = 90 * (1 - ((self.__right_animation_frame - (self.__animation_duration // 2)) / (self.__animation_duration // 2)))

            self.__arm_angles.right_flipper_in_degrees = angle

            self.__right_animation_frame += 1

            if self.__right_animation_frame > self.__animation_duration:
                self.__right_animation_frame = 0

            glut.glutPostRedisplay()

    def special_key_press(self, key: int) -> None:
        camera = self.__cam

        match key:
            case glut.GLUT_KEY_UP:
                camera.position[1] += +1

            case glut.GLUT_KEY_DOWN:
                camera.position[1] -= 1

            case glut.GLUT_KEY_LEFT:
                self.__theta_xz += 2
                camera.update_position_by_polar_system(self.__theta_xz)

            case glut.GLUT_KEY_RIGHT:
                self.__theta_xz -= 2
                camera.update_position_by_polar_system(self.__theta_xz)
   