import pygame, sys, random
from screen import GameWindow
from Test_codes import display_menu
pygame.init()


class Anomaly:
    game_window = GameWindow(1920, 1080, "Avoid the Obstacle")
    
    display_menu(game_window.win, game_window.width, game_window.height)
    enemyCar5 = pygame.image.load('enemyCar5.png').convert_alpha()
    enemyCar5 = pygame.transform.scale(enemyCar5, (40, 70))
    enemyCar8 = pygame.image.load('enemyCar8.png').convert_alpha()
    enemyCar8 = pygame.transform.scale(enemyCar8, (50, 90))
    enemyCar9 = pygame.image.load('enemyCar9.png').convert_alpha()
    enemyCar9 = pygame.transform.scale(enemyCar9, (40, 70))
    enemyCar10 = pygame.image.load('enemyCar10.png').convert_alpha()
    enemyCar10 = pygame.transform.scale(enemyCar10, (40, 70))
    enemyCar11 = pygame.image.load('enemyCar11.png').convert_alpha()
    enemyCar11 = pygame.transform.scale(enemyCar11, (40, 70))
    enemyCar12 = pygame.image.load('enemyCar12.png').convert_alpha()
    enemyCar12 = pygame.transform.scale(enemyCar12, (40, 70))
    enemyCar13 = pygame.image.load('enemyCar13.png').convert_alpha()
    enemyCar13 = pygame.transform.scale(enemyCar13, (40, 70))
    enemyCar14 = pygame.image.load('enemyCar14.png').convert_alpha()
    enemyCar14 = pygame.transform.scale(enemyCar14, (40, 70))
    enemyCar16 = pygame.image.load('enemyCar16.png').convert_alpha()
    enemyCar16 = pygame.transform.scale(enemyCar16, (40, 70))
    enemyCar18 = pygame.image.load('enemyCar18.png').convert_alpha()
    enemyCar18 = pygame.transform.scale(enemyCar18, (40, 70))
    enemyCar19 = pygame.image.load('enemyCar19.png').convert_alpha()
    enemyCar19 = pygame.transform.scale(enemyCar19, (40, 70))
    enemyCar20 = pygame.image.load('enemyCar20.png').convert_alpha()
    enemyCar20 = pygame.transform.scale(enemyCar20, (40, 70))
    enemyCar21 = pygame.image.load('enemyCar21.png').convert_alpha()
    enemyCar21 = pygame.transform.scale(enemyCar21, (40, 70))
    enemyCar22 = pygame.image.load('enemyCar22.png').convert_alpha()
    enemyCar22 = pygame.transform.scale(enemyCar22, (40, 70))
    enemyCar23 = pygame.image.load('enemyCar23.png').convert_alpha()
    enemyCar23 = pygame.transform.scale(enemyCar23, (40, 70))
    enemyCar24 = pygame.image.load('enemyCar24.png').convert_alpha()
    enemyCar24 = pygame.transform.scale(enemyCar24, (40, 70))


    obstacle_car_images = [enemyCar5, enemyCar8, enemyCar9, enemyCar10, enemyCar11, 
                           enemyCar12, enemyCar13, enemyCar14, enemyCar16, enemyCar18, enemyCar19, 
                           enemyCar20, enemyCar21, enemyCar22, enemyCar23, enemyCar24]
    