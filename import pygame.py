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

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

def main():
    game_window = GameWindow(1920, 1080, "Avoid the Obstacle")
    enemyCar1 = pygame.image.load('enemyCar1.png')
    enemyCar1 = pygame.transform.scale(enemyCar1, (90, 90))
    enemyCar2 = pygame.image.load('enemyCar2.png')
    enemyCar2 = pygame.transform.scale(enemyCar2, (90, 90))
    enemyCar3 = pygame.image.load('enemyCar3.png')
    enemyCar3 = pygame.transform.scale(enemyCar3, (90, 90))
    enemyCar4 = pygame.image.load('enemyCar4.png')
    enemyCar4 = pygame.transform.scale(enemyCar4, (90, 90))
    obstacle_car_images = [enemyCar1, enemyCar2, enemyCar3, enemyCar4]

    man = player_test(910, 850, 90, 90)
    collision1 = 810
    collision2 = 1200
    enemies = [Obstacle(random.randrange(collision1, collision2), -random.randint(0, game_window.height), 90, 90, random.choice(obstacle_car_images)) for _ in range(3)]
    running = True

    # Timer for speed increase
    speed_increase_timer = 0
    speed_increase_interval = 2000  # Increase speed every 5000 milliseconds (5 seconds)
    speed_increase_factor = 1.07  # Increase speed by 5% every interval

    # Speed limits
    max_scroll_speed = 40
    max_obstacle_speed = 60
    max_player_speed = 20

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
