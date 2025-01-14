import pygame
import sys


driveRight = [
    pygame.image.load('r1.png'),
    pygame.image.load('r2.png'),
    pygame.image.load('r3.png'),
    pygame.image.load('r4.png'),
    pygame.image.load('r5.png'),
]

driveLeft = [
    pygame.image.load('l1.png'),
    pygame.image.load('l2.png'),
    pygame.image.load('l3.png'),
    pygame.image.load('l4.png'),
    pygame.image.load('l5.png'),
]



car = pygame.image.load('straight.png')
# enemy_car = pygame.image.load('enemyCar.png')

class player_test(object):
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