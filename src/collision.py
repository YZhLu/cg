import math

# Coordenadas e dimensões da bola
ball_radius = 1.0
ball_position = [0.0, 1.0, 0.0]
ball_velocity = [0.1, 0.0, 0.1]  # Exemplo de velocidade da bola

# Coordenadas e dimensões da parede
wall_position = [0.0, 0.0, 0.0]
wall_dimensions = [5.0, 10.0, 1.0]
wall_inclination = 45.0  # Ângulo de inclinação da parede em graus

def check_collision():
    # Verificar se a bola está dentro dos limites da parede
    ball_x, ball_y, ball_z = ball_position
    wall_x, wall_y, wall_z = wall_position
    wall_width, wall_height, wall_depth = wall_dimensions

    # Converter o ângulo de inclinação para radianos
    wall_inclination_rad = math.radians(wall_inclination)

    # Calcular as coordenadas da bola no sistema de coordenadas da parede
    ball_x_wall = (ball_x - wall_x) * math.cos(wall_inclination_rad) - (ball_y - wall_y) * math.sin(wall_inclination_rad)
    ball_y_wall = (ball_x - wall_x) * math.sin(wall_inclination_rad) + (ball_y - wall_y) * math.cos(wall_inclination_rad)

    # Verificar a colisão entre a bola e a parede
    if (wall_x - wall_width / 2 <= ball_x_wall <= wall_x + wall_width / 2) and \
       (wall_y - wall_height / 2 <= ball_y_wall <= wall_y + wall_height / 2) and \
       (wall_z - wall_depth / 2 <= ball_z <= wall_z + wall_depth / 2):
        # Colisão detectada
        print("Colisão detectada entre a bola e a parede!")

        # Tome as ações apropriadas, como inverter a direção da bola

# Loop principal de renderização
while True:
    # Atualizar a posição da bola com base na velocidade
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    ball_position[2] += ball_velocity[2]

    # Verificar a colisão a cada iteração
    check_collision()

    # Renderizar a cena OpenGL

    # Resto do código de renderização...
