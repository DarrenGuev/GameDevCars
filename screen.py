import pygame
import sys

class GameWindow:
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height), pygame.SRCALPHA)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('bg124.png')
        self.bg_width = self.bg_image.get_width()
        self.bg_height = self.bg_image.get_height()
        self.bg_x = (self.width - self.bg_width) // 2  # Adjusted for centering
        self.scroll_speed = 15
        self.score = 0
        self.font = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 36)
        self.bg_segments = self.init_background_segments()
        
    def init_background_segments(self):
        segments = []
        num_segments = (self.height // self.bg_height) + 2
        for i in range(num_segments):
            y = i * self.bg_height - self.bg_height
            segments.append({'y': y, 'image': self.bg_image.copy()})
        return segments

    def update_background(self):
        for segment in self.bg_segments:
            segment['y'] += self.scroll_speed
            self.win.blit(segment['image'], (self.bg_x, segment['y']))
        for segment in self.bg_segments:
            if segment['y'] >= self.height:
                min_y = min(seg['y'] for seg in self.bg_segments)
                segment['y'] = min_y - self.bg_height
    
    def draw_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        text_rect = score_text.get_rect()
        text_rect.center = (1800, 50)
        self.win.blit(score_text, text_rect)
        
    def redraw_game_window(self, man, enemies):
        self.win.fill((119, 119, 119))
        self.update_background()
        man.draw(self.win)
        for enemy in enemies:
            enemy.draw(self.win)
        self.draw_score()
        pygame.display.update()

    def increase_score(self):
        self.score += 10

class HighscoreManager:
    def __init__(self, filepath="highscore.txt"):
        self.filepath = filepath
        self.highscores = self.load_highscores()
        self.font = pygame.font.Font(None, 20)

    def load_highscores(self):
        try:
            with open(self.filepath, "r") as file:
                return [int(score.strip()) for score in file.readlines()]
        except FileNotFoundError:
            return [0] * 5  # Default top 5 scores

    def update_highscores(self, score):
        self.highscores.append(score)
        self.highscores = sorted(self.highscores, reverse=True)[:5]  # Keep top 5 scores
        with open(self.filepath, "w") as file:
            file.writelines(f"{s}\n" for s in self.highscores)

    def display_highscores(self, win, font, width, height):
        """Display highscores in the center of the screen"""
        highscore_text = font.render("Top 5 Highscores:", True, (255, 255, 255))
        win.blit(highscore_text, (50, 90))

        for i, score in enumerate(self.highscores):
            highscore_entry = font.render(f"{i + 1}. {score}", True, (255, 255, 255))
            win.blit(highscore_entry, (50, 140 + i * 65))