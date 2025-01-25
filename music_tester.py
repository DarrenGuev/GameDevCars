import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Define a music class
class Music:
    def __init__(self):
        pygame.mixer.music.load('feel_it.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
        print("Playing music...")

# Create an instance of the Music class
music = Music()

# Wait for the user to press Enter to quit
input("Press Enter to quit...")

# Quit Pygame
pygame.quit()