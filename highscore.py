import pygame
import os

# Initialize pygame
pygame.init()

# Set up the screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("High Score Example")

# Set up fonts
font = pygame.font.SysFont(None, 36)

# File to store the high score
highscore_file = "highscore.txt"

# Function to load the high score from file
def load_highscore():
    if os.path.exists(highscore_file):
        with open(highscore_file, "r") as file:
            return int(file.read())
    return 0

# Function to save the high score to file
def save_highscore(score):
    with open(highscore_file, "w") as file:
        file.write(str(score))

# Game loop
def game():
    running = True
    score = 0
    highscore = load_highscore()
    
    while running:
        screen.fill((0, 0, 0))  # Clear the screen

        # Check for events (close window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Simulate the game score increasing
        score += 1
        if score > highscore:
            highscore = score
            save_highscore(score)

        # Display the score and high score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        highscore_text = font.render(f"High Score: {highscore}", True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(highscore_text, (10, 50))

        pygame.display.update()  # Update the display

        pygame.time.delay(1000)  # Simulate a delay, like a game frame

    pygame.quit()

# Start the game
game()
