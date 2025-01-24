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
        self.mask = self.create_mask(image)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def create_mask(self, image):
        return pygame.mask.from_surface(image)


def check_collision(player, enemy):
    player_mask = player.mask
    enemy_mask = enemy.mask
    offset_x = enemy.x - player.x
    offset_y = enemy.y - player.y
    return player_mask.overlap(enemy_mask, (offset_x, offset_y)) is not None


def display_game_over(win, width, height, score):
    """Display the Game Over screen"""
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    restart_button = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
    quit_button = pygame.Rect(width // 2 - 100, height // 2 + 150, 200, 50)

    while True:
        win.fill((0, 0, 0))  # Black background
        win.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 4))
        win.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 3))

        # Draw buttons
        pygame.draw.rect(win, (0, 255, 0), restart_button)  # Green Restart button
        pygame.draw.rect(win, (255, 0, 0), quit_button)  # Red Quit button

        # Button text
        restart_text = font.render("Restart", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))
        win.blit(restart_text, (restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2,
                                restart_button.y + restart_button.height // 2 - restart_text.get_height() // 2))
        win.blit(quit_text, (quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2,
                             quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    return "restart"  # Restart the game
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


def main():
    pygame.init()
    game_window = GameWindow(1920, 1080, "Avoid the Obstacle")

    display_menu(game_window.win, game_window.width, game_window.height)

    enemy_images = [pygame.image.load(f'enemyCar{i}.png').convert_alpha() for i in range(5, 19)]
    enemy_images = [pygame.transform.scale(img, (40, 70)) for img in enemy_images]

    player = player_test(910, 850, 90, 90)
    obstacles = [Obstacle(random.randint(700, 1100), -random.randint(0, game_window.height), 90, 90, random.choice(enemy_images)) for _ in range(4)]

    running = True
    score = 0

    while running:
        game_window.clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 700 - player.width - player.vel:
            player.x -= player.vel
        if keys[pygame.K_RIGHT] and player.x < 1100 - player.width - player.vel:
            player.x += player.vel

        # Move obstacles and check collisions
        for obstacle in obstacles:
            obstacle.y += obstacle.obstacle_speed
            if obstacle.y > game_window.height:
                obstacle.y = -random.randint(0, 300)
                obstacle.x = random.randint(700, 1100)
                score += 1  # Increase score when an obstacle resets

            if check_collision(player, obstacle):
                # Game Over - show Game Over screen
                action = display_game_over(game_window.window, game_window.width, game_window.height, score)
                if action == "restart":
                    return main()  # Restart the game
                else:
                    running = False

        game_window.redraw_game_window(player, obstacles)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
