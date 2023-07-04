class BallPosition:
    """
    A classe que representa os angulos das juntas dos flippers
    """
    __sphere_radius: float  # Raio da esfera
    __sphere_position: list # Posição inicial da esfera (x, y, z)
    __sphere_velocity: list # Velocidade inicial da esfera (vx, vy, vz)
    __gravity: float        # Força gravitacional na direção x crescente

    def __init__(self) -> None:
        
        self.__sphere_radius = 0.50  # Raio da esfera
        self.__sphere_position = [1.6, 1.0, 3.2]  # Posição inicial da esfera (x, y, z)
        self.__sphere_velocity = [0.0, 0.0, 0.0]  # Velocidade inicial da esfera (vx, vy, vz)
        self.__gravity = 0.01  

    #Funções que capturam os valores correspondentes no ball controler 

    @property
    def sphere_radius(self) -> float:
        return self.__sphere_radius
    
    @property
    def sphere_position(self) -> list:
        return self.__sphere_position
    
    @property
    def sphere_velocity(self) -> list:
        return self.__sphere_velocity
    
    @property
    def gravity(self) -> float:
        return self.__gravity
    
    #Atualiza o raio da bola
    @sphere_radius.setter
    def sphere_radius(self, radius: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        self.__sphere_radius = radius
        return self.__sphere_radius
    
    #Atualiza a gravidade
    @sphere_position.setter
    def sphere_position(self, position: list) -> list:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        self.__sphere_position = position
        return self.__sphere_position
    
    #Atualiza o raio da bola
    @sphere_velocity.setter
    def sphere_velocity(self, velocity: list) -> list:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        self.__sphere_velocity = velocity
        return self.__sphere_velocity
    
    #Atualiza a gravidade
    @gravity.setter
    def gravity(self, gravity: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        self.__gravity = gravity
        return self.__gravity
