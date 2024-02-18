import pygame

class Projectile:
    def __init__(self, x, y, speed):
        self.projectile_image = pygame.image.load('assets/images/projectile.png')
        self.rect = self.projectile_image.get_rect()
        self.rect.center = (x, y)

        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)