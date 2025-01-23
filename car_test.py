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
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.image = pygame.image.load('straight.png')  # Load the player image
        self.mask = self.create_mask(self.image)  # Create mask for player

    def draw(self, win):
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
            win.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def create_mask(self, image):
        """Create a mask for the player car to handle transparency"""
        return pygame.mask.from_surface(image)
