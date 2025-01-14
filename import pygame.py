# Initialize pygame
import pygame
import sys
from car_test import player_test
import random
pygame.init()

# Screen code
clock = pygame.time.Clock()
screen_height = 1080
screen_width = 1920
win = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Avoid the Obstacle")

# Load background
background_image = pygame.image.load('bg.jpg')
background_width = background_image.get_width()
background_height = background_image.get_height()
# Create a list to store background segments
background_segments = []
# Calculate how many segments we need to cover screen + 1 extra to prevent a gap
num_segments = (screen_height // background_height) + 2

# Initialize background positions
# Start with one segment above the screen to ensure smooth scrolling
for i in range(num_segments):
    y = i * background_height - background_height
    background_segments.append({'y': y, 'image': background_image.copy()})

# Calculate position to center the background
bg_x = (screen_width - background_width) // 2.83

# Calculate scroll speed
scroll_speed = 15

# UI Elements
score = 0
font = pygame.font.Font(None, 36)

class Obstacle(object):
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obstacle_speed = 10
        self.image = image

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

def redraw_game_window():
    # Fill screen with gray first to avoid artifacts
    win.fill((119, 119, 119))
    
    # Update and draw background segments
    for segment in background_segments:
        # Update position
        segment['y'] += scroll_speed
        
        # Draw the segment
        win.blit(segment['image'], (bg_x, segment['y']))
    
    # Check if any segment has moved entirely below the screen
    for segment in background_segments:
        if segment['y'] >= screen_height:
            # Find the highest segment (smallest y value)
            min_y = min(seg['y'] for seg in background_segments)
            # Place this segment above the highest segment, precisely aligned
            segment['y'] = min_y - background_height
    
    man.draw(win)
    for enemy in enemies:
        enemy.draw(win)

    # Draw Score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = score_text.get_rect()
    text_rect.center = (770, 50)
    win.blit(score_text, text_rect)

    pygame.display.update()

# Load different car images for the player and obstacles, resize to 90x90
enemyCar1 = pygame.image.load('enemyCar1.png')
enemyCar1 = pygame.transform.scale(enemyCar1, (120, 120))

enemyCar2 = pygame.image.load('enemyCar2.png')
enemyCar2 = pygame.transform.scale(enemyCar2, (120, 120))

enemyCar3 = pygame.image.load('enemyCar3.png')
enemyCar3 = pygame.transform.scale(enemyCar3, (120, 120))

enemyCar4 = pygame.image.load('enemyCar4.png')
enemyCar4 = pygame.transform.scale(enemyCar4, (120, 120))

obstacle_car_images = [enemyCar1, enemyCar2, enemyCar3, enemyCar4]

man = player_test(720, 650, 90, 90)
running = True

# Create multiple enemy objects with different images, same size as player car
enemies = [Obstacle(random.randrange(640, 960), -random.randint(0, screen_height), 90, 90, random.choice(obstacle_car_images)) for _ in range(3)]

while running:
    collision1 = 640
    collision2 = 960
    clock.tick(24)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > collision1 - man.width - man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < collision2 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0
    
    # Update Score (Example: Increase score over time)
    score += 1 

    for enemy in enemies:
        enemy.y += enemy.obstacle_speed
        if enemy.y > screen_height:
            enemy.y = 0 - enemy.height
            enemy.x = random.randrange(640, 960)
            enemy.image = random.choice(obstacle_car_images)
            score += 10  # Award points for successfully dodging an enemy
    
    redraw_game_window()

# Quit
pygame.quit()
sys.exit()