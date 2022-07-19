from sys import exit
import pygame

pygame.init()
# Para Desplegar el canvas
canvas = pygame.display.set_mode((800, 400))

# Para nombrar la pantalla
pygame.display.set_caption('Dinosour game')

# Para colocar la cantidad de FPS por segundo
Clock = pygame.time.Clock()

# Nueva superficie
# test_surface = pygame.Surface((400, 200))
# test_surface.fill('Red')

test_font = pygame.font.Font('Fonts/Origin.ttf', 50)

Background = pygame.image.load('Graphics/fondo_contacto.png').convert()
Ground = pygame.image.load('Graphics/ground.png').convert_alpha()
text_surface = test_font.render('My game', False, 'Black')

Enemy_surface = pygame.image.load('Graphics/Cube.png').convert_alpha()
Enemy_x_position = 400
Player_surface = pygame.image.load('Graphics/player1.png').convert_alpha()
true_value = True

while true_value:
    # Para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Para generar la superficie
    canvas.blit(Background, (0, 0))
    Enemy_x_position -= 4
    if Enemy_x_position == -500:
        Enemy_x_position = 600
    canvas.blit(Enemy_surface, (Enemy_x_position, 200))
    canvas.blit(Ground, (0, 75))
    canvas.blit(text_surface, (300, 60))
    canvas.blit(Player_surface, (80, 140))

    # Para actualizar y a cuantos FPS
    pygame.display.update()
    Clock.tick(60)
