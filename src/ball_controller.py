from OpenGL import GLUT as glut
from ball_position import BallPosition
import math
import numpy as np

class BallController:
    __ball_position: BallPosition
    __damping_factor: float
    __lSlope: bool
    __rSlope: bool
    
    
    def __init__(self, position: BallPosition) -> None:
        self.__ball_position = position
        self.__damping_factor = 0.95  # Valor de amortecimento (ajuste conforme necessário)
        self.__lSlope = False
        self.__rSlope = False
    
    
    def update_sphere(self) -> None:
        
        # Calcula a força resultante na direção da rampa

        if (not self.__lSlope and not self.__rSlope):
            self.__ball_position.sphere_velocity[0] += self.__ball_position.gravity  # Aplica a força gravitacional na direção x crescente
            self.__ball_position.sphere_position[0] += self.__ball_position.sphere_velocity[0]  # Atualiza a posição da esfera na direção x
            #self.__ball_position.sphere_velocity[2] += self.__ball_position.sphere_velocity[2]# * self.__atrator  # Aplica a força gravitacional na direção x crescente
            #self.__ball_position.sphere_position[2] += self.__ball_position.sphere_velocity[2]  # Atualiza a posição da esfera na direção x
        
        self.check_bottom_colision()
        self.check_left_colision()
        self.check_top_colision()
        self.check_right_colision()
        self.check_left_slope_colision()
        self.check_right_slope_colision()
        self.check_bumper_collision()
        
        # Calcula o fator de amortecimento com base na direção da velocidade
        self.__damping_factor = 0.95 if self.__ball_position.sphere_velocity[0] > 0 else 0.9
        # Aplica o amortecimento na velocidade da esfera
        self.__ball_position.sphere_velocity[0] *= self.__damping_factor
        self.__ball_position.sphere_velocity[2] *= self.__damping_factor

        
        glut.glutPostRedisplay()    
    
   
    
    bumpers = [(-9.0, -2.0, 0.75), (-9, 2, 1.0), (2, -3.0, 1.0), (2, 3.0, 1.0), (-15, 0, 0.5), (-2, 0, 0.75), (-12, 6, 0.75), (-5, -4.5, 0.75), (-5, 4.5, 0.75), (12, -6, 0.75)]
    lCageX1 = -18
    lCageX2 = 0
    lCageZ = 9
    rCageX1 = -18
    rCageX2 = 0
    rCageZ = -9
    tCageX = -18
    tCageZ1 = 9
    tCageZ2 = -9
    lSCageX1 = 0
    lSCageX2 = 5.6
    lSCageZ1 = 9
    lSCageZ2 = 3.4
    rSCageX1 = 0
    rSCageX2 = 5.6
    rSCageZ2 = -9
    rSCageZ1 = -3.4
    bCageX = 8
    bCageZ1 = 3
    bCageZ2 = -3
    flipper 
    #(pos = [-9, 0, 2],  size = [0.75, 2, 1.0])
    #(pos = [-9, 0, -2],  size = [1.0, 2, 0.75])
    
    # (size = [0.2, 2, 1.25], pos = [-1.8, 0, -5.8], )
    # (size = [0.2, 2, 1.25], pos = [-1.8, 0, 5.8], )
    
    def check_top_colision(self) -> None:
        if (self.__ball_position.sphere_position[0] < self.tCageX - self.__ball_position.sphere_radius):
            self.__ball_position.sphere_position[0] = self.tCageX + self.__ball_position.sphere_radius# Aplica a força gravitacional na direção x crescente
            print("top")
            
    def check_bottom_colision(self) -> None:
        if (self.__ball_position.sphere_position[0] > self.bCageX + self.__ball_position.sphere_radius):
            self.__ball_position.sphere_position[0] = self.lCageZ #+ self.__ball_position.sphere_radius# Aplica a força gravitacional na direção x crescente
        
            print("bottom")
            
    def check_left_colision(self) -> None:
        if (self.__ball_position.sphere_position[0] < self.lCageX2 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[0] > self.lCageX1 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[2] > self.lCageZ - self.__ball_position.sphere_radius):
            self.__ball_position.sphere_position[2] = self.lCageZ - self.__ball_position.sphere_radius# Aplica a força gravitacional na direção x crescente
        
            print("left")
    
    def check_right_colision(self) -> None:
        if (self.__ball_position.sphere_position[0] < self.rCageX2 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[0] > self.rCageX1 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[2] < self.rCageZ + self.__ball_position.sphere_radius):
            self.__ball_position.sphere_position[2] = self.rCageZ + self.__ball_position.sphere_radius# Aplica a força gravitacional na direção x crescente
            
            print("right", self.__ball_position.sphere_position)
    
    def check_left_slope_colision(self) -> None:
        if (self.__ball_position.sphere_position[0] < self.lSCageX2 + self.__ball_position.sphere_radius and self.__ball_position.sphere_position[0] > self.lSCageX1 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[2] < self.lSCageZ1 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[2] > self.lSCageZ2 - self.__ball_position.sphere_radius*2):
            self.__lSlope = True
           
            # Calcula a força resultante na direção da rampa
            ramp_angle = math.radians(45)  # Ângulo de inclinação da rampa (ajuste conforme necessário)
            ramp_force = self.__ball_position.gravity * math.sin(ramp_angle)
            
            # Aplica a força resultante na direção da rampa à velocidade da esfera
            self.__ball_position.sphere_velocity[0] += ramp_force * 0.7
            self.__ball_position.sphere_velocity[2] += ramp_force

            # Atualiza a posição da esfera na direção x e z com base na velocidade da esfera
            self.__ball_position.sphere_position[0] += self.__ball_position.sphere_velocity[0]
            self.__ball_position.sphere_position[2] -= self.__ball_position.sphere_velocity[2]
           
            print("left slope")
        else:
            # if(self.__slope == True):
            #     self.__ball_position.sphere_position[0] = self.__ball_position.sphere_position[0]
            #     self.__ball_position.sphere_position[2] = self.__ball_position.sphere_position[2]
            
            self.__lSlope = False
    
    def check_right_slope_colision(self) -> None:
        if (self.__ball_position.sphere_position[0] < self.rSCageX2 + self.__ball_position.sphere_radius and self.__ball_position.sphere_position[0] > self.rSCageX1 - self.__ball_position.sphere_radius and self.__ball_position.sphere_position[2] < self.rSCageZ1 + self.__ball_position.sphere_radius*2 and self.__ball_position.sphere_position[2] > self.rSCageZ2 + self.__ball_position.sphere_radius):
            self.__rSlope = True
           
            # Calcula a força resultante na direção da rampa
            ramp_angle = math.radians(45)  # Ângulo de inclinação da rampa (ajuste conforme necessário)
            ramp_force = self.__ball_position.gravity * math.sin(ramp_angle)
            
            # Aplica a força resultante na direção da rampa à velocidade da esfera
            self.__ball_position.sphere_velocity[0] += ramp_force * 0.7
            self.__ball_position.sphere_velocity[2] += ramp_force

            # Atualiza a posição da esfera na direção x e z com base na velocidade da esfera
            self.__ball_position.sphere_position[0] += self.__ball_position.sphere_velocity[0]
            self.__ball_position.sphere_position[2] += self.__ball_position.sphere_velocity[2]
           
            print("right slope")
        else:
            # if(self.__slope == True):
            #     self.__ball_position.sphere_position[0] = self.__ball_position.sphere_position[0]
            #     self.__ball_position.sphere_position[2] = self.__ball_position.sphere_position[2]
                
            self.__rSlope = False
    
    def check_bumper_collision(self) -> None:
        print(self.__ball_position.sphere_velocity[2])
        for bumper in self.bumpers:
            bumper_radius = bumper[2]  # Raio do bumper
            
            # Calcula a distância entre a esfera e o bumper
            distance = np.sqrt((self.__ball_position.sphere_position[0] - bumper[0]) ** 2 + (self.__ball_position.sphere_position[2] - bumper[1]) ** 2)
            
            if distance < bumper_radius:
                
                # A colisão ocorreu
                
                # Ajusta a velocidade da esfera para simular o efeito de retorno
                self.__ball_position.sphere_velocity[0] *= -1  # Inverte a direção da velocidade na direção x
                self.__ball_position.sphere_velocity[2] *= -1  # Inverte a direção da velocidade na direção z
                
                # Atualiza a posição da esfera para evitar que fique presa dentro do bumper
                self.__ball_position.sphere_position[0] += self.__ball_position.sphere_velocity[0] * 0.1
                self.__ball_position.sphere_position[2] += self.__ball_position.sphere_velocity[2] * 30
                
                # Calcula a direção da colisão com base na velocidade antes da colisão
                collision_direction = np.array([-self.__ball_position.sphere_velocity[0], 0, -self.__ball_position.sphere_velocity[2]])
                collision_direction /= np.linalg.norm(collision_direction)  # Normaliza o vetor de direção da colisão

                # Rotaciona a bola em 45 graus em torno do eixo y
                rotation_angle = math.radians(45)
                rotation_matrix = np.array([[math.cos(rotation_angle), 0, math.sin(rotation_angle)],
                                            [0, 1, 0],
                                            [-math.sin(rotation_angle), 0, math.cos(rotation_angle)]])

                
                new_direction = np.dot(rotation_matrix, collision_direction)
                
                self.__ball_position.sphere_velocity[0] = -new_direction[0]
                self.__ball_position.sphere_velocity[2] = -new_direction[2]

    def check_flipper_colision(self) -> None:

        distance = np.sqrt(self.__ball_position.sphere_position[0] - )
