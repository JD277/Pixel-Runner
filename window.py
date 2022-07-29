import random
from sys import exit
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        Player_walk1 = pygame.image.load('Graphics/p1_walk02.png').convert_alpha()
        Player_walk2 = pygame.image.load('Graphics/p1_walk03.png').convert_alpha()
        self.Player_Jump = pygame.image.load('Graphics/p1_jump.png').convert_alpha()

        self.Player_walk = [Player_walk1, Player_walk2]
        self.Player_index = 0

        self.image = self.Player_walk[self.Player_index]
        self.rect = self.image.get_rect(topleft = (120, 255))
        self.gravity = 0

    def Player_input(self):
        Key = pygame.key.get_pressed()
        if Key[pygame.K_SPACE] and self.rect.bottom >= 350:
            self.gravity = -20

    def aply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 350: self.rect.bottom = 350

    def animation_state(self):
       if self.rect.bottom < 350:
            self.image = self.Player_Jump
       else:
           self.Player_index += 0.1
           if self.Player_index > len(self.Player_walk):
            self.Player_index = 0
           self.image = self.Player_walk[int(self.Player_index)]

    def update(self):
        self.Player_input()
        self.aply_gravity()
        self.animation_state()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame1 = pygame.image.load('Graphics/flyFly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('Graphics/flyFly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            Snail_surface = pygame.image.load('Graphics/snailWalk1.png').convert_alpha()
            Snail_surface2 = pygame.image.load('Graphics/snailWalk2.png').convert_alpha()
            self.frames = [Snail_surface, Snail_surface2]
            y_pos = 340
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1100), y_pos))

    def animtion_state(self):
        self.animation_index += 0.1
        if self.animation_index > len(self.frames) : self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animtion_state()
        self.rect.x -= 6
        self.destroy()



def Display_score():
    current_time = int(pygame.time.get_ticks() /1000) - Start_time
    Score_surf = test_font.render(f'Score: {current_time}', False, 'Black')
    Score_rect = Score_surf.get_rect(center = (400, 50))
    canvas.blit(Score_surf,Score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacles_group,False):
        obstacles_group.empty()
        return False
    else: return True

pygame.init()
# Para Desplegar el canvas
canvas = pygame.display.set_mode((800, 400))

# Para nombrar la pantalla
icon = pygame.image.load('Graphics/p3_duck.png')
pygame.display.set_caption('Pixel Runner')
pygame.display.set_icon(icon)
# Para colocar la cantidad de FPS por segundo
Clock = pygame.time.Clock()

test_font = pygame.font.Font('Fonts/Origin.ttf', 50)
Background = pygame.image.load('Graphics/fondo_contacto.png').convert()
Ground = pygame.image.load('Graphics/ground.png').convert_alpha()
bg_music = pygame.mixer.Sound('Graphics/Jeremy Renner - _The Medicine_ (Lyric Video)(MP3_70K).mp3')
bg_music.set_volume(0.3)
bg_music.play(loops=-1)
#groups---------------------------------------------------------------------
obstacles_group = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()
player.add(Player())
#----------------------------------------------------------------------------
Game_active = False
Start_time  = 0
Score = 0
#----------------------------------------------------------------------------
Inst_surface = test_font.render("Press ''space'' to start the game", False, '#98caff')
Inst_rect = Inst_surface.get_rect(center= (620,350))
Inst_surface = pygame.transform.rotozoom(Inst_surface,0,0.5)

Inst_surface2 = test_font.render("Pixel Runner", False, '#98caff')
Inst_surface2 = pygame.transform.rotozoom(Inst_surface2,0,0.5)
Inst_rect2 = Inst_surface2.get_rect(center= (400,40))
#----------------------------------------------------------------------------
Player_stand = pygame.image.load('Graphics/p1_jump.png').convert_alpha()
Player_stand= pygame.transform.scale2x(Player_stand)
Player_rect2 = Player_stand.get_rect(center = (400,200))


#----------------------------------------------------------------------------
true_value = True
#Timer
obstacule_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacule_timer,1500)

Snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(Snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

while true_value:
    # Para cerrar la ventana
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if Game_active:
            #Timers-----------------------------------------------------------
            if event.type == obstacule_timer:
                obstacles_group.add(Obstacles(random.choice(['fly','snail', 'snail','snail'])))


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Game_active = True
                Start_time = int(pygame.time.get_ticks() / 1000)

    if Game_active:
        # Para generar la superficie
        canvas.blit(Background, (0, 0))
        canvas.blit(Ground, (0, 75))
        Score = Display_score()

        #-----------------------------------------

        player.draw(canvas)
        player.update()

        obstacles_group.draw(canvas)
        obstacles_group.update()
        #-----------------------------------------
        Game_active = collision_sprite()
    else:
        canvas.fill('#3e3f53')
        canvas.blit(Player_stand,Player_rect2)
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
