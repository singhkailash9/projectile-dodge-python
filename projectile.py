import pygame

class Projectile:
    def __init__(self, x, y, speed):
        self.speed = speed
        self.rect = pygame.Rect(x, y, 10, 10)

    def move(self):
        self.rect.move_ip(0, self.speed)