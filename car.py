import pygame
import sys
import random

driveRight = [
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\r1.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\r2.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\r3.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\r4.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\r5.png'),
]

driveLeft = [
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\l1.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\l2.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\l3.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\l4.png'),
    pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\l5.png'),
]



car = pygame.image.load(r'C:\Users\kence\Desktop\CAR GAME\GameDevCars\Super Car Red\straight.png')
# enemy_car = pygame.image.load('enemyCar.png')

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
            
        if self.left:
             win.blit(driveLeft[self.walkCount//3], (self.x,self.y))
             if self.walkCount < 12:
                 self.walkCount += 1

        elif self.right:
            win.blit(driveRight[self.walkCount//3], (self.x,self.y))
            if self.walkCount < 12:
                self.walkCount += 1
        else:
            win.blit(car, (self.x, self.y))

class obstacle(object):
    def __init__(self, obs_y, width, height):
        self.x = random.randrange(200,650)
        self.y = obs_y
        self.width = width
        self.height = height
        self.bumped = False
        self.x_change = 0
        self.obstacle_speed = 10
        self.obs = 0
        self.y_change = 0


