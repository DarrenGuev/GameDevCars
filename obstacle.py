import pygame
import sys
import random


class obstacle(object):
    def __init__(self, obs_y, width, height):
        self.x = random.randrange(640,960)
        self.y = obs_y
        self.width = width
        self.height = height
        self.bumped = False
        self.x_change = 0
        self.obstacle_speed = 10
        self.obs = 0
        self.y_change = 0