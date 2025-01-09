import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixelated Racing Game")


# Button Class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen, mouse_pos):
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, current_color, self.rect)
        text_surface = FONT.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]

# Create Buttons
start_button = Button(20, 100, 150, 50, "Start", GRAY, WHITE)
instruction_button = Button(20, 200, 150, 50, "Instructions", GRAY, WHITE)
quit_button = Button(20, 300, 150, 50, "Quit", GRAY, WHITE)

# Game Loop Variables
running = True
game_active = False

# Main Game Loop
while running:
    screen.fill(BLACK)

    # Get Mouse Position and State
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if not game_active:
        # Draw Buttons
        start_button.draw(screen, mouse_pos)
        instruction_button.draw(screen, mouse_pos)
        quit_button.draw(screen, mouse_pos)

        # Check Button Clicks
        if start_button.is_clicked(mouse_pos, mouse_pressed):
            game_active = True
        elif instruction_button.is_clicked(mouse_pos, mouse_pressed):
            print("Instructions: Use arrow keys to move the car!")
        elif quit_button.is_clicked(mouse_pos, mouse_pressed):
            running = False

    else:
        # Draw Gameplay Area
        pygame.draw.rect(screen, GREEN, (200, 0, 400, SCREEN_HEIGHT))

        # Draw Right Panel (Fuel and Score)
        pygame.draw.rect(screen, BLUE, (620, 0, 180, SCREEN_HEIGHT))
        fuel_text = FONT.render("Fuel: 100%", True, WHITE)
        score_text = FONT.render("Score: 0", True, WHITE)
        screen.blit(fuel_text, (630, 50))
        screen.blit(score_text, (630, 100))

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the Display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
