import pygame

# Pong Game created in Python

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self, direction):
        # loop movement direction
        if direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed


class Ball:
    def __init__(self, x, y, width, height, speed, direction_x, direction_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction_x = direction_x
        self.direction_y = direction_y

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

    def collide(self, paddle):
        if self.x >= paddle.x and self.x <= paddle.x + paddle.width:
            if self.y >= paddle.y and self.y <= paddle.y + paddle.height:
                return True
        return False


class Game(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ball = Ball(self.width / 2, self.height / 2, 10, 10, 5, 1, 1)
        self.paddle_1 = Paddle(0, self.height / 2 - 50, 10, 100, 15)
        self.paddle_2 = Paddle(self.width - 10, self.height / 2 - 50, 10, 100, 15)
        self.score_1 = 0
        self.score_2 = 0

    def draw(self, window):
        window.fill((0, 0, 0))
        self.ball.draw(window)
        self.paddle_1.draw(window)
        self.paddle_2.draw(window)
        font = pygame.font.SysFont("monospace", 35)
        text_1 = font.render(str(self.score_1), True, (255, 255, 255))
        text_2 = font.render(str(self.score_2), True, (255, 255, 255))
        window.blit(text_1, (self.width / 2 - 50, self.height / 2 - 50))
        window.blit(text_2, (self.width / 2 + 50, self.height / 2 - 50))

    def update(self):
        self.ball.move()
        if self.ball.x <= 0:
            self.score_2 += 1
            self.ball.x = self.width / 2
            self.ball.y = self.height / 2
            self.ball.direction_x = 1
            self.ball.direction_y = 1
        if self.ball.x >= self.width - 10:
            self.score_1 += 1
            self.ball.x = self.width / 2
            self.ball.y = self.height / 2
            self.ball.direction_x = -1
            self.ball.direction_y = 1
        if self.ball.y <= 0 or self.ball.y >= self.height - 10:
            self.ball.direction_y *= -1
        if self.ball.collide(self.paddle_1):
            self.ball.direction_x *= -1
        if self.ball.collide(self.paddle_2):
            self.ball.direction_x *= -1

    def moveHandler(self, event):
        # loop move when key is being held down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.paddle_1.move("UP")
            if event.key == pygame.K_s:
                self.paddle_1.move("DOWN")
            if event.key == pygame.K_UP:
                self.paddle_2.move("UP")
            if event.key == pygame.K_DOWN:
                self.paddle_2.move("DOWN")

    def run(self):
        pygame.init()
        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong")
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.moveHandler(event)
            self.update()
            self.draw(window)
            pygame.display.update()


game = Game(800, 600)
game.run()