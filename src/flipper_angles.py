class FlipperAngles:
    """
    A classe que representa os angulos das juntas dos flippers
    """
    __left_flipper_in_degrees: float
    __right_flipper_in_degrees: float

    def __init__(self) -> None:
        
        self.__left_flipper_in_degrees = 0
        self.__right_flipper_in_degrees = 0

    #Funções que capturam os valores correspondentes no keyboard controler 

    @property
    def left_flipper_in_degrees(self) -> float:
        return self.__left_flipper_in_degrees
    
    @property
    def right_flipper_in_degrees(self) -> float:
        return self.__right_flipper_in_degrees
    
    #Atualiza os ângulos dos flippers
    @left_flipper_in_degrees.setter
    def left_flipper_in_degrees(self, angle_in_degrees: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        self.__left_flipper_in_degrees = angle_in_degrees
        return self.__left_flipper_in_degrees
    
    @right_flipper_in_degrees.setter
    def right_flipper_in_degrees(self, angle_in_degrees: float) -> float:
        """
            atualiza e retorna o angulo da garra mas só atualiza se o angulo for válido.
        """
        self.__right_flipper_in_degrees = angle_in_degrees
        return self.__right_flipper_in_degrees
