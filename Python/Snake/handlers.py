import random;
import pygame;

class Handlers:
    def __init__(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_speed = 15
        self.food_pos = [random.randrange(1, 70) * 10, random.randrange(1, 50) * 10]
        self.food_spawn = True
        self.score = 0
        self.direction = "RIGHT"
        self.size = (700, 500)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("My Game")
        self.fps = pygame.time.Clock()