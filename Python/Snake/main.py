import random;
import pygame;

class Game:
    def __init__(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_speed = 20
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
        pygame.display.set_caption("Snake")
        self.fps = pygame.time.Clock()

    def update(self):
        self.screen.fill(self.BLACK)
        self.draw_snake()
        self.draw_food()
        self.check_collision()
        self.check_score()

        # draw Score if player is alive
        if self.food_spawn:
            font = pygame.font.SysFont("monospace", 35)
            text = font.render("Score: " + str(self.score), True, self.WHITE)
            self.screen.blit(text, (0, 0))

        pygame.display.update()
        self.fps.tick(self.snake_speed)

    def draw_snake(self):
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    def draw_food(self):
        if self.food_spawn:
            pygame.draw.rect(self.screen, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
        else:
            self.food_pos = [random.randrange(1, 70) * 10, random.randrange(1, 50) * 10]
            self.food_spawn = True

    def check_collision(self):
        if self.snake_pos[0] > 690 or self.snake_pos[0] < 0:
            self.game_over()
        if self.snake_pos[1] > 490 or self.snake_pos[1] < 0:
            self.game_over()
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                self.game_over()

    def game_over(self):
        # game over centered position
        self.screen.fill(self.BLACK)
        font = pygame.font.SysFont("monospace", 35)
        text = font.render("Game Over", True, self.RED)
        text_rect = text.get_rect()
        text_rect.center = (350, 250)
        self.screen.blit(text, text_rect)

        # score centered position
        text = font.render("Score: " + str(self.score), True, self.RED)
        text_rect.center = (350, 300)
        self.screen.blit(text, text_rect)

        self.food_spawn = False

    def check_score(self):
        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            self.food_spawn = False
            self.snake_speed += 1
            self.score += 1
            self.snake_body.append([0, 0])

    def get_direction(self, event):
        if event.key == pygame.K_RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"
        if event.key == pygame.K_LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        if event.key == pygame.K_UP and self.direction != "DOWN":
            self.direction = "UP"
        if event.key == pygame.K_DOWN and self.direction != "UP":
            self.direction = "DOWN"

    def update_snake(self):
        if self.direction == "RIGHT":
            self.snake_pos[0] += 10
        if self.direction == "LEFT":
            self.snake_pos[0] -= 10
        if self.direction == "UP":
            self.snake_pos[1] -= 10
        if self.direction == "DOWN":
            self.snake_pos[1] += 10
        self.snake_body.insert(0, list(self.snake_pos))
        if len(self.snake_body) > self.score + 1:
            del self.snake_body[-1]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.get_direction(event)
            self.update_snake()
            self.update()


game = Game()
game.start()
game.run()