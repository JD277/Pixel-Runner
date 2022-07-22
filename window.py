from sys import exit
import pygame

pygame.init()
# Para Desplegar el canvas
canvas = pygame.display.set_mode((800, 400))

# Para nombrar la pantalla
pygame.display.set_caption('Dinosour game')

# Para colocar la cantidad de FPS por segundo
Clock = pygame.time.Clock()

test_font = pygame.font.Font('Fonts/Origin.ttf', 50)
Background = pygame.image.load('Graphics/fondo_contacto.png').convert()
Ground = pygame.image.load('Graphics/ground.png').convert_alpha()
#----------------------------------------------------------------------------
Game_active = True
#----------------------------------------------------------------------------
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
        if Game_active:
            if event.type == pygame.MOUSEBUTTONDOWN :
                hola = event.pos
                if Player_rect.collidepoint(hola) and Player_rect.bottom == 350:
                    Player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Player_rect.bottom == 350:
                    Player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Game_active = True
                Enemy_rect.x = 810
    if Game_active:
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
        if Player_rect.bottom >= 350:
            Player_rect.bottom = 350
        canvas.blit(Player_surface,Player_rect)
        #-----------------------------------------

        if Enemy_rect.colliderect(Player_rect):
            Game_active = False

    else:
        canvas.fill('Gold')

    # Para actualizar y a cuantos FPS
    pygame.display.update()
    Clock.tick(60)
