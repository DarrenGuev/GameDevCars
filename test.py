import pygame
import sys
from car_test import player_test
import random
from screen import GameWindow

class Obstacle:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obstacle_speed = 10
        self.image = image
        self.mask = self.create_mask(image)  # Create mask for the obstacle

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def create_mask(self, image):
        """Create a mask from the given image to handle transparency"""
        return pygame.mask.from_surface(image)

def check_collision(player, enemy):
    """Check for pixel-perfect collision using masks"""
    player_mask = player.mask
    enemy_mask = enemy.mask

    # Get the offset between the player and the enemy
    offset_x = enemy.x - player.x
    offset_y = enemy.y - player.y

    # Check if the masks overlap (collision)
    return player_mask.overlap(enemy_mask, (offset_x, offset_y)) is not None

def display_menu(win, width, height):
    """Display a start menu with Start and Quit buttons"""
    font = pygame.font.Font(None, 74)
    title_text = font.render("Avoid the Obstacle", True, (255, 255, 255))
    start_button = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50)
    quit_button = pygame.Rect(width // 2 - 100, height // 2 + 20, 200, 50)

    while True:
        win.fill((0, 0, 0))  # Black background
        win.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))

        # Draw buttons
        pygame.draw.rect(win, (0, 255, 0), start_button)  # Green button for Start
        pygame.draw.rect(win, (255, 0, 0), quit_button)  # Red button for Quit

        # Button text
        start_text = font.render("Start", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))
        win.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                              start_button.y + start_button.height // 2 - start_text.get_height() // 2))
        win.blit(quit_text, (quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2,
                             quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    return  # Start the game
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

def main():
    pygame.init()
    game_window = GameWindow(1920, 1080, "Avoid the Obstacle")

    display_menu(game_window.window, game_window.width, game_window.height)


    game_window = GameWindow(1920, 1080, "Avoid the Obstacle")
    enemyCar5 = pygame.image.load('enemyCar5.png').convert_alpha()
    enemyCar5 = pygame.transform.scale(enemyCar5, (40, 70))
    enemyCar8 = pygame.image.load('enemyCar8.png').convert_alpha()
    enemyCar8 = pygame.transform.scale(enemyCar8, (50, 90))
    enemyCar9 = pygame.image.load('enemyCar9.png').convert_alpha()
    enemyCar9 = pygame.transform.scale(enemyCar9, (40, 70))
    enemyCar10 = pygame.image.load('enemyCar10.png').convert_alpha()
    enemyCar10 = pygame.transform.scale(enemyCar10, (40, 70))
    enemyCar11 = pygame.image.load('enemyCar11.png').convert_alpha()
    enemyCar11 = pygame.transform.scale(enemyCar11, (40, 70))
    enemyCar12 = pygame.image.load('enemyCar12.png').convert_alpha()
    enemyCar12 = pygame.transform.scale(enemyCar12, (40, 70))
    enemyCar13 = pygame.image.load('enemyCar13.png').convert_alpha()
    enemyCar13 = pygame.transform.scale(enemyCar13, (40, 70))
    enemyCar14 = pygame.image.load('enemyCar14.png').convert_alpha()
    enemyCar14 = pygame.transform.scale(enemyCar14, (40, 70))
    enemyCar16 = pygame.image.load('enemyCar16.png').convert_alpha()
    enemyCar16 = pygame.transform.scale(enemyCar16, (40, 70))
    enemyCar18 = pygame.image.load('enemyCar18.png').convert_alpha()
    enemyCar18 = pygame.transform.scale(enemyCar18, (40, 70))

    obstacle_car_images = [enemyCar5, enemyCar8, enemyCar9, enemyCar10, enemyCar11, 
                           enemyCar12, enemyCar13, enemyCar14, enemyCar16, enemyCar18]
    
    man = player_test(910, 850, 90, 90)
    collision1 = 830
    collision2 = 1250
    enemies = [Obstacle(random.randrange(collision1, collision2), -random.randint(0, game_window.height), 90, 90, random.choice(obstacle_car_images)) for _ in range(4)]
    running = True

    # Timer for speed increase
    speed_increase_timer = 0
    speed_increase_interval = 10  # Increase speed
    speed_increase_factor = 1.0005  # Increase speed by 5% every interval

    # Speed limits
    max_scroll_speed = 40
    max_obstacle_speed = 60
    max_player_speed = 20
    
    # Main game loop
    while running:
        game_window.clock.tick(30)

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

        game_window.increase_score()

        for enemy in enemies:
            enemy.y += enemy.obstacle_speed
            if enemy.y > game_window.height:
                enemy.y = 0 - enemy.height
                enemy.x = random.randrange(700, 1100)
                enemy.image = random.choice(obstacle_car_images)
                enemy.mask = enemy.create_mask(enemy.image)  # Re-create the mask after resetting image

            # Check for pixel-perfect collision between player and enemy using masks
            if check_collision(man, enemy):
                print("Collision detected!")
                running = False  # Stop the game if collision occurs

        # Increase game speed over time
        speed_increase_timer += game_window.clock.get_time()
        if speed_increase_timer >= speed_increase_interval:
            game_window.scroll_speed = min(game_window.scroll_speed * speed_increase_factor, max_scroll_speed)
            for enemy in enemies:
                enemy.obstacle_speed = min(enemy.obstacle_speed * speed_increase_factor, max_obstacle_speed)
            man.vel = min(man.vel * speed_increase_factor, max_player_speed)
            speed_increase_timer = 0

        game_window.redraw_game_window(man, enemies)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
