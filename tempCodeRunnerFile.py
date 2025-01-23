class Obstacle(object):
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obstacle_speed = 10
        self.image = image

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))