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
text_rect = text_surface.get_rect(center= (400,50))
#----------------------------------------------------------------------------
Enemy_surface = pygame.image.load('Graphics/snailWalk1.png').convert_alpha()
Enemy_rect = Enemy_surface.get_rect(midbottom = (720, 340))
#----------------------------------------------------------------------------
Player_surface = pygame.image.load('Graphics/p1_front.png').convert_alpha()
Player_rect = Player_surface.get_rect(topleft = (80, 255))
Player_gravity = 0
#----------------------------------------------------------------------------
true_value = True

while true_value:
    # Para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            hola = event.pos
            if Player_rect.collidepoint(hola) :
                Player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player_gravity = -20

    # Para generar la superficie
    canvas.blit(Background, (0, 0))
    canvas.blit(Ground, (0, 75))
    canvas.blit(text_surface, text_rect)
    #-----------------------------------------
    Enemy_rect.right = Enemy_rect.right - 4
    if Enemy_rect.x <= -100:
        Enemy_rect.x = 810
    canvas.blit(Enemy_surface, Enemy_rect)
    #-----------------------------------------
    Player_gravity += 1
    Player_rect.y += Player_gravity
    canvas.blit(Player_surface,Player_rect)
    #-----------------------------------------
    #Collisions
    #if Player_rect.colliderect(Enemy_rect):
     #   print('collision')
    #Keyboard input
    #Keys = pygame.key.get_pressed()
    #if Keys[pygame.K_SPACE]:
        #print('Jump')


    # Para actualizar y a cuantos FPS
    pygame.display.update()
    Clock.tick(60)
