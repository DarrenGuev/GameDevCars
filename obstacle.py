import pygame
import sys
import random

class obstacle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obstacle_speed = 20
        self.obs = 0
        self.y_change = 0
        self.obs_x = random.randrange(400, 1200)
        self.obstac = pygame.image.load('enemyCar.png')