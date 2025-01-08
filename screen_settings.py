import sys
import pygame
from car import player

man = player(720, 650, 64, 64)

def display_screen():
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

    # Calculate how many segments we need to cover screen + 1 extra to prevent gaps
    num_segments = (screen_height // background_height) + 2

    # Initialize background positions
    # Start with one segment above the screen to ensure smooth scrolling
    for i in range(num_segments):
        y = i * background_height - background_height
        background_segments.append({'y': y, 'image': background_image.copy()})

    # Calculate position to center the background
    bg_x = (screen_width - background_width) // 2.83