import pygame
import sys
from car import player

# Initialize pygame
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

# Calculate how many segments we need to cover screen + 1 extra to prevent 
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

def draw_start_menu():
    """Draw the start menu with Start and Quit buttons."""
    win.fill((0, 0, 0))  # Fill background with black

    # Draw title
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Avoid the Obstacle", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
    win.blit(title_text, title_rect)

    # Draw buttons
    button_font = pygame.font.Font(None, 48)

    start_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 80)
    quit_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 100, 300, 80)

    pygame.draw.rect(win, (0, 128, 0), start_button)
    pygame.draw.rect(win, (128, 0, 0), quit_button)

    start_text = button_font.render("Start Game", True, (255, 255, 255))
    quit_text = button_font.render("Quit Game", True, (255, 255, 255))

    win.blit(start_text, start_button.move(50, 15).topleft)
    win.blit(quit_text, quit_button.move(50, 15).topleft)

    pygame.display.update()

    return start_button, quit_button

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

    # Draw Score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = score_text.get_rect()
    text_rect.center = (screen_width // 2, 50)
    win.blit(score_text, text_rect)

    pygame.display.update()

# Start Menu
man = player(720, 650, 64, 64)
running = True
game_active = False

while running:
    if not game_active:
        # Draw the start menu
        start_button, quit_button = draw_start_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_active = True
                elif quit_button.collidepoint(event.pos):
                    running = False
    else:
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

        redraw_game_window()

# Quit
pygame.quit()
sys.exit()
