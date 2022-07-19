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
Background = pygame.image.load('Graphics/fondo_contacto.png')
Ground = pygame.image.load('Graphics/ground.png')
true_value = True

while true_value:
    # Para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Para generar la superficie
    canvas.blit(Background, (0, 0))
    canvas.blit(Ground,(0,75))
    pygame.display.update()
    Clock.tick(60)
