
from camera import Camera
from OpenGL import GLUT as glut
from flipper_angles import FlipperAngles

"""
    Teclas que controlam os ângulos do braço e a câmera.
    Essa classe foi criada para a FlipperAngles não depender do OpenGL para atualizar os ângulos.
    M-V-C
"""
class KeyboardController:
    __arm_angles: FlipperAngles
    __cam: Camera
    __claw_in_degrees = 0
    __theta_xz = 0

    def __init__(self, arm: FlipperAngles, cam: Camera) -> None:
        self.__arm_angles = arm
        self.__cam = cam

    def key_press(self, key: bytes) -> None:

        match key.decode():
            case 'A':
                self.__arm_angles.shoulder_in_degrees += 5
                self.__arm_angles.left_flipper_in_degrees += 5

            case 'a':
                self.__arm_angles.shoulder_in_degrees -= 5
                self.__arm_angles.left_flipper_in_degrees -= 5
            
            case 'D':
                #self.__arm_angles.shoulder_in_degrees += 5
                self.__arm_angles.right_flipper_in_degrees += 5

            case 'd':
                #self.__arm_angles.shoulder_in_degrees -= 5
                self.__arm_angles.right_flipper_in_degrees -= 5

            case 'S':
                self.__arm_angles.elbow_in_degrees += 5

            case 's':
                self.__arm_angles.elbow_in_degrees -= 5

            case 'B':
                self.__arm_angles.base_in_degrees += 5

            case 'b':
                self.__arm_angles.base_in_degrees -= 5

            case 'C':
                angle = self.__claw_in_degrees + 5
                self.__claw_in_degrees = self.__arm_angles.set_angle_claw(
                    angle)

            case 'c':
                angle = self.__claw_in_degrees - 5
                self.__claw_in_degrees = self.__arm_angles.set_angle_claw(
                    angle)

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
