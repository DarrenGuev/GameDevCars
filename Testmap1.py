import pygame
import sys
from car import player

# Initialize pygame
pygame.init()
from screen_settings import display_screen
display_screen()

# Calculate scroll speed
scroll_speed = 15
def redraw_game_window():
    # Fill screen with gray first to avoid artifacts
    display_screen.win.fill((119, 119, 119))
    
    # Update and draw background segments
    for segment in display_screen.background_segments:
        # Update position
        segment['y'] += scroll_speed
        
        # Draw the segment
        display_screen.win.blit(segment['image'], (display_screen.bg_x, segment['y']))
    
    # Check if any segment has moved entirely below the screen
    for segment in display_screen.background_segments:
        if segment['y'] >= display_screen.screen_height:
            # Find the highest segment (smallest y value)
            min_y = min(seg['y'] for seg in display_screen.background_segments)
            # Place this segment above the highest segment, precisely aligned
            segment['y'] = min_y - display_screen.background_height
    
    man.draw(display_screen.win)
    pygame.display.update()

# Main game loop
man = player(720, 650, 64, 64)
running = True

while running:
    display_screen.clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < display_screen.screen_width - man.width - man.vel:
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


