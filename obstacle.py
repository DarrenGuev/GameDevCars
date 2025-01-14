import pygame
import sys
import random

class obstacle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obstacle_speed = 10
        self.obs = 0
        self.y_change = 0
        self.obs_x = random.randrange(640, 960)
        self.obstac = pygame.image.load('enemyCar.png')