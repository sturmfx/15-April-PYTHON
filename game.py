import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ОХОТА НА КРУЖКИ")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYER_RADIUS = 20
TARGET_RADIUS = 10
TARGET_COUNT = 5
SPEED = 2
PLAYER_SPEED = 1
FPS = 60


class Target:
    def __init__(self):
        self.x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
        self.y = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
        self.dx = random.choice([-SPEED, SPEED])
        self.dy = random.choice([-SPEED, SPEED])

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        if self.x < TARGET_RADIUS or self.x > WIDTH - TARGET_RADIUS:
            self.dx = -self.dx
        if self.y < TARGET_RADIUS or self.y > HEIGHT - TARGET_RADIUS:
            self.dy = -self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), TARGET_RADIUS)


targets = [Target() for _ in range(TARGET_COUNT)]

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_x, player_y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, BLUE, (player_x, player_y), PLAYER_RADIUS)

    for target in targets:
        target.move()
        target.draw(screen)

        distance = ((player_x - target.x) ** 2 + (player_y - target.y) ** 2) ** 0.5
        if distance < PLAYER_RADIUS + TARGET_RADIUS:
            targets.remove(target)
            targets.append(Target())
    pygame.display.flip()

pygame.quit()
