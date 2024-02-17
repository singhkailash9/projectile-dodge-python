import pygame, random, sys
from projectile import Projectile
from score import Score

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 690

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.player_rect = pygame.Rect(self.screen_width / 2 - 10, self.screen_height / 2 - 10, 20, 20)

        self.projectiles = []

        self.score = 0
        self.score_manager = Score()
        self.high_score = self.score_manager.high_score

        self.game_over = False

    def reset_game(self):
        self.score = 0
        self.game_over = False
        self.player_rect.center = (self.screen_width / 2, self.screen_height / 2)
        self.projectiles.clear()

    def game_over_screen(self):
        self.game_over = True
        self.score_manager.save_score(self.score)
        # update high_score again to display changes without breaking main loop in run_game
        self.high_score = self.score_manager.high_score

        self.screen.fill("black")
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(game_over_text, (450, 300))

        font = pygame.font.Font(None, 36)
        final_score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(final_score_text, (500, 400))

        high_score_text = font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
        self.screen.blit(high_score_text, (500, 450))

        retry_text = font.render("Press R to Retry", True, (255, 255, 255))
        self.screen.blit(retry_text, (500, 500))

        exit_text = font.render("Press Esc to Exit", True, (255, 255, 255))
        self.screen.blit(exit_text, (500, 550))
        pygame.display.flip()

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.game_over:
                self.game_over_screen()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:  # Retry
                            self.reset_game()
                        elif event.key == pygame.K_ESCAPE:  # Quit
                            pygame.quit()
                            sys.exit()
            else:
                self.screen.fill("purple")

                pygame.draw.rect(self.screen, "red", self.player_rect)

                keys = pygame.key.get_pressed()
                move_distance = 300 * self.dt
                if keys[pygame.K_w]:
                    self.player_rect.y -= move_distance
                if keys[pygame.K_s]:
                    self.player_rect.y += move_distance
                if keys[pygame.K_a]:
                    self.player_rect.x -= move_distance
                if keys[pygame.K_d]:
                    self.player_rect.x += move_distance
                if keys[pygame.K_SPACE]:
                    self.player_rect.y -= 1.5 * move_distance

                if pygame.time.get_ticks() % 2 == 0:
                    next_projectile = random.randint(2, self.screen_width)
                    new_projectile = Projectile(next_projectile, 0, 3)
                    self.projectiles.append(new_projectile)
                    self.score += 1

                for projectile in self.projectiles:
                    projectile.move()
                    pygame.draw.rect(self.screen, "white", projectile.rect)

                    # Collision detection between the player and projectiles
                    if self.player_rect.colliderect(projectile.rect):
                        self.game_over_screen()

                # Score display
                font = pygame.font.Font(None, 36)
                score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
                self.screen.blit(score_text, (10, 10))

                pygame.display.flip()

                self.dt = self.clock.tick(60) / 1000

pygame.quit()