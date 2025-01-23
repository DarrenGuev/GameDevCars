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

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

def main():
    game_window = GameWindow(1920, 1080, "Avoid the Obstacle")
    enemyCar1 = pygame.image.load('enemyCar1.png')
    enemyCar1 = pygame.transform.scale(enemyCar1, (140, 140))
    enemyCar2 = pygame.image.load('enemyCar2.png')
    enemyCar2 = pygame.transform.scale(enemyCar2, (110, 120))
    enemyCar3 = pygame.image.load('enemyCar3.png')
    enemyCar3 = pygame.transform.scale(enemyCar3, (100, 130))
    enemyCar4 = pygame.image.load('enemyCar4.png')
    enemyCar4 = pygame.transform.scale(enemyCar4, (140, 140))
    enemyCar5 = pygame.image.load('enemyCar5.png')
    enemyCar5 = pygame.transform.scale(enemyCar5, (40, 70))
    enemyCar6 = pygame.image.load('enemyCar6.png')
    enemyCar6 = pygame.transform.scale(enemyCar6, (40, 70))
    enemyCar8 = pygame.image.load('enemyCar8.png')
    enemyCar8 = pygame.transform.scale(enemyCar8, (50, 90))
    enemyCar9 = pygame.image.load('enemyCar9.png')
    enemyCar9 = pygame.transform.scale(enemyCar9, (40, 70))
    enemyCar10 = pygame.image.load('enemyCar10.png')
    enemyCar10 = pygame.transform.scale(enemyCar10, (40, 70))
    enemyCar11 = pygame.image.load('enemyCar11.png')
    enemyCar11 = pygame.transform.scale(enemyCar11, (40, 70))
    enemyCar12 = pygame.image.load('enemyCar12.png')
    enemyCar12 = pygame.transform.scale(enemyCar12, (40, 70))
    enemyCar13 = pygame.image.load('enemyCar13.png')
    enemyCar13 = pygame.transform.scale(enemyCar13, (40, 70))
    enemyCar14 = pygame.image.load('enemyCar14.png')
    enemyCar14 = pygame.transform.scale(enemyCar14, (40, 70))
    enemyCar15 = pygame.image.load('enemyCar15.png')
    enemyCar15 = pygame.transform.scale(enemyCar15, (40, 70))
    enemyCar16 = pygame.image.load('enemyCar16.png')
    enemyCar16 = pygame.transform.scale(enemyCar16, (40, 70))
    enemyCar17 = pygame.image.load('enemyCar17.png')
    enemyCar17 = pygame.transform.scale(enemyCar17, (40, 70))
    enemyCar18 = pygame.image.load('enemyCar18.png')
    enemyCar18 = pygame.transform.scale(enemyCar18, (40, 70))
    obstacle_car_images = [enemyCar1, enemyCar2, enemyCar3, enemyCar4, enemyCar5,
                           enemyCar6, enemyCar8, enemyCar9, enemyCar10, enemyCar11, 
                           enemyCar12, enemyCar13, enemyCar14, enemyCar15, enemyCar16, 
                           enemyCar17, enemyCar18]

    man = player_test(910, 850, 90, 90)
    collision1 = 810
    collision2 = 1200
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

            # Check for collision between player and enemy
            if man.get_rect().colliderect(enemy.get_rect()):
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
