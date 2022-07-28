import random
from sys import exit
import pygame


def Display_score():
    current_time = int(pygame.time.get_ticks() /1000) - Start_time
    Score_surf = test_font.render(f'Score: {current_time}', False, 'Black')
    Score_rect = Score_surf.get_rect(center = (400, 50))
    canvas.blit(Score_surf,Score_rect)
    return current_time

def obstacle_movement(obstacle_list) :
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x = obstacle_rect.x - 5
            if Score >= 10:
                obstacle_rect.x = obstacle_rect.x - 7

            if obstacle_rect.bottom == 340:
                canvas.blit(Enemy_surface, obstacle_rect)
            else:
                canvas.blit(fly_surface, obstacle_rect)
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collision(Player, obstacles) :
    if obstacles:
        for obstacles_rect in obstacles:
            if Player.colliderect(obstacles_rect):
                return False

    return True



pygame.init()
# Para Desplegar el canvas
canvas = pygame.display.set_mode((800, 400))

# Para nombrar la pantalla
pygame.display.set_caption('Pixel Runner')

# Para colocar la cantidad de FPS por segundo
Clock = pygame.time.Clock()

test_font = pygame.font.Font('Fonts/Origin.ttf', 50)
Background = pygame.image.load('Graphics/fondo_contacto.png').convert()
Ground = pygame.image.load('Graphics/ground.png').convert_alpha()
#----------------------------------------------------------------------------
Game_active = False
Start_time  = 0
#----------------------------------------------------------------------------
Inst_surface = test_font.render("Press ''space'' to start the game", False, '#98caff')
Inst_rect = Inst_surface.get_rect(center= (620,350))
Inst_surface = pygame.transform.rotozoom(Inst_surface,0,0.5)

Inst_surface2 = test_font.render("Pixel Runner", False, '#98caff')
Inst_surface2 = pygame.transform.rotozoom(Inst_surface2,0,0.5)
Inst_rect2 = Inst_surface2.get_rect(center= (400,40))
#----------------------------------------------------------------------------
Enemy_surface = pygame.image.load('Graphics/snailWalk1.png').convert_alpha()
obstacle_rect_list = []

fly_surface = pygame.image.load('Graphics/flyFly1.png').convert_alpha()

#----------------------------------------------------------------------------
Player_surface = pygame.image.load('Graphics/p1_front.png').convert_alpha()
Player_rect = Player_surface.get_rect(topleft = (80, 255))
Player_gravity = 0

Player_stand = pygame.image.load('Graphics/p1_jump.png').convert_alpha()
Player_stand= pygame.transform.scale2x(Player_stand)
Player_rect2 = Player_stand.get_rect(center = (400,200))

Score = 0
#----------------------------------------------------------------------------
true_value = True
#Timer
obstacule_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacule_timer,900)

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
                Start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacule_timer and Game_active == True:
            if random.randint(0,2):
                obstacle_rect_list.append(Enemy_surface.get_rect(
                    midbottom = (random.randint(900, 1100), 340)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(
                    midbottom = (random.randint(900, 1100), 210)))

    if Game_active:
        # Para generar la superficie
        canvas.blit(Background, (0, 0))
        canvas.blit(Ground, (0, 75))
        Score = Display_score()
        #-----------------------------------------
        #Enemy_rect.right = Enemy_rect.right - 4
        #if Enemy_rect.x <= -100:
        #    Enemy_rect.x = 810
        #canvas.blit(Enemy_surface, Enemy_rect)
        #-----------------------------------------
        Player_gravity += 1
        Player_rect.y += Player_gravity
        if Player_rect.bottom >= 350:
            Player_rect.bottom = 350
        canvas.blit(Player_surface,Player_rect)
        #-----------------------------------------
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        #-----------------------------------------
        Game_active = collision(Player_rect,obstacle_rect_list)


    else:
        canvas.fill('#3e3f53')
        canvas.blit(Player_stand,Player_rect2)
        obstacle_rect_list.clear()
        Player_rect.topleft = (80, 255)
        Player_gravity = 0
        Score_message = test_font.render(f'Your score: {Score}', False,'#98caff')
        Score_message_rect = Score_message.get_rect(center = (500,350))
        Score_message = pygame.transform.rotozoom(Score_message, 0, 0.5)
        canvas.blit(Inst_surface2,Inst_rect2)

        if Score == 0:
            canvas.blit(Inst_surface,Inst_rect)
        else:
            canvas.blit(Score_message,Score_message_rect)

    # Para actualizar y a cuantos FPS
    pygame.display.update()
    Clock.tick(60)
