import pygame
import sys
from car import player

# Initialize pygame
pygame.init()

# Screen code
clock = pygame.time.Clock()
screen_heigth = 1080
screen_width = 1920
win = pygame.display.set_mode((screen_width, screen_heigth), pygame.FULLSCREEN)
pygame.display.set_caption("Avoid the Obstacle")

# Load background
background1 = pygame.image.load('bg.jpg')
background2 = pygame.image.load('bg.jpg')


# Get background dimensions
bg1_width = background1.get_width()
bg1_height = background1.get_height()

bg2_width = background2.get_width()
bg2_height = background2.get_height()

total_bg_width = bg1_width + bg2_width


start_x = (screen_width - total_bg_width) // 2
bg1_x = start_x
bg2_x = start_x + bg1_width

# Calculate position to center the background
bg1_x = (screen_width - bg1_width) // 2.83
bg1_y = (screen_heigth - bg1_height) // 700

# Calculate position to center the background
bg2_x = (screen_width - bg2_width) // 2.83
bg2_y = (screen_heigth - bg2_height) // 1.5

def redraw_game_window():
    # Fill screen with gray first to avoid artifacts
    win.fill((119, 119, 119))
    # Draw centered background
    win.blit(background1, (bg1_x, bg1_y))
    win.blit(background2, (bg2_x, bg2_y))

    man.draw(win)
    pygame.display.update()

# Main game loop
man = player(720, 650, 64, 64)
running = True
while running:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
<<<<<<< HEAD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Add escape key to exit
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        
=======

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        running = False
 

    if keys[pygame.K_LEFT] and man.x > man.vel: 
        man.x -= man.vel 
        man.left = True
        man.right = False
>>>>>>> 01d2c28efc66cb768e2b730170a196a5e11cc5c8
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True

    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    redraw_game_window()

# Quit
pygame.quit()
sys.exit()