from sys import exit
from turtle import Screen
import pygame


pygame.init()

canvas = pygame.display.set_mode((800,400))
pygame.display.set_caption('Dinosour game')
Clock = pygame.time.Clock()

test_surface = pygame.Surface((400,200))
test_surface.fill('Red')
true_value = True

while true_value: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    Screen.blit
    
    pygame.display.update()
    Clock.tick(60)