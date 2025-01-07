import pygame
import sys
from car import player

#screen code
clock = pygame.time.Clock()
screen_heigth = 1080
screen_width = 1920
win = pygame.display.set_mode((screen_width, screen_heigth), pygame.FULLSCREEN)
pygame.display.set_caption("Avoid the Obstacle")

win.fill ((119,119,119))
pygame.display.update()
background = pygame.image.load('bg.png')

def redraw_game_window():
    win.blit(background,(0,0))
    man.draw(win)
    pygame.display.update()

#main game loop
man = player(300, 410, 64, 64)
running = True
while running:
    clock.tick(27)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    


    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_LEFT] and man.x > man.vel: 
        man.x -= man.vel 
        man.left = True
        man.right = False 
        
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        man.x += man.vel 
        man.left = False
        man.right = True 

    else: 
        man.left = False 
        man.right = False 
        man.walkCount = 0

    redraw_game_window()
    

#quit
pygame.quit()


