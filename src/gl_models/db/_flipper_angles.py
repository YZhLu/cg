class FlipperAngles:
    """
    A classe que representa os angulos das juntas do braço robótico
    """
    __base_in_degrees: float
    __shoulder_in_degrees: float
    __elbow_in_degrees: float
    __claw_in_degrees: float
    __left_flipper_in_degrees: float
    __right_flipper_in_degrees: float

    def __init__(self) -> None:
        self.__base_in_degrees = 0
        self.__shoulder_in_degrees = 0
        self.__elbow_in_degrees = 0
        self.__claw_in_degrees = 0
        self.__left_flipper_in_degrees = 0
        self.__right_flipper_in_degrees = 0

    #Funções que capturam os valores correspondentes no keyboard controler 
    @property
    def base_in_degrees(self) -> float:
        return self.__base_in_degrees

    @property
    def shoulder_in_degrees(self) -> float:
        return self.__shoulder_in_degrees

    @property
    def elbow_in_degrees(self) -> float:
        return self.__elbow_in_degrees

    @property
    def upper_claw_in_degrees(self) -> float:
        return -self.__claw_in_degrees

    @property
    def bottom_claw_in_degrees(self) -> float:
        return self.__claw_in_degrees

    @property
    def left_flipper_in_degrees(self) -> float:
        return self.__left_flipper_in_degrees
    
    @property
    def right_flipper_in_degrees(self) -> float:
        return self.__right_flipper_in_degrees
    
    #Atualiza os ângulos das partes do robô, se estiver dentro dos máximos e mínimos definidos

    @base_in_degrees.setter
    def base_in_degrees(self, angle_in_degrees: float) -> float:
        """atualiza o angulo da base mas só se o angulo for válido."""

        if 0 <= angle_in_degrees <= 360:
            self.__base_in_degrees = angle_in_degrees

    @shoulder_in_degrees.setter
    def shoulder_in_degrees(self, angle_in_degrees: float) -> None:
        """atualiza o angulo do ombro mas só se o angulo for válido."""
        #print(angle_in_degrees)
        if True or 0 <= angle_in_degrees <= 180:
            self.__shoulder_in_degrees = angle_in_degrees

    @elbow_in_degrees.setter
    def elbow_in_degrees(self, angle_in_degrees: float):
        """atualiza o angulo do cotovelo mas só se o angulo for válido."""

        if 0 <= angle_in_degrees <= 135:
            self.__elbow_in_degrees = angle_in_degrees
    
    def set_angle_claw(self, angle_in_degrees: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        if 0 <= angle_in_degrees <= 17:
            self.__claw_in_degrees = angle_in_degrees

        return self.__claw_in_degrees
    
    @left_flipper_in_degrees.setter
    def left_flipper_in_degrees(self, angle_in_degrees: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        print(angle_in_degrees)
        #if 0 <= angle_in_degrees <= 17:
        self.__left_flipper_in_degrees = angle_in_degrees
        return self.__left_flipper_in_degrees
    
    @right_flipper_in_degrees.setter
    def right_flipper_in_degrees(self, angle_in_degrees: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        print(angle_in_degrees)
        #if 0 <= angle_in_degrees <= 17:
        self.__right_flipper_in_degrees = angle_in_degrees
        return self.__right_flipper_in_degrees
