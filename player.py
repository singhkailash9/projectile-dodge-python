import pygame

class Player:
    def __init__(self, screen_w, screen_h):
        self.dt = 0
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.player_image = pygame.image.load('assets/images/player.png')
        self.player_rect = self.player_image.get_rect()
        self.player_rect.center = (self.screen_w // 2, self.screen_h // 2)

    def move(self, keys):
        move_distance = 300 * self.dt

        if keys[pygame.K_w] and self.player_rect.y - move_distance >= 0:
            self.player_rect.y -= move_distance

        if keys[pygame.K_s] and self.player_rect.y + move_distance + self.player_rect.height <= self.screen_h:
            self.player_rect.y += move_distance

        if keys[pygame.K_a] and self.player_rect.x - move_distance >= 0:
            self.player_rect.x -= move_distance

        if keys[pygame.K_d] and self.player_rect.x + move_distance + self.player_rect.width <= self.screen_w:
            self.player_rect.x += move_distance

        if keys[pygame.K_SPACE]:
            self.player_rect.y -= 1.5 * move_distance
