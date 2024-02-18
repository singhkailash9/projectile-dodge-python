import pygame

class Screen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    def game_over_screen(self, score, high_score):
        self.screen.fill("black")
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(game_over_text, (450, 300))

        font = pygame.font.Font(None, 36)
        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        self.screen.blit(final_score_text, (500, 400))

        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        self.screen.blit(high_score_text, (500, 450))

        retry_text = font.render("Press R to Retry", True, (255, 255, 255))
        self.screen.blit(retry_text, (500, 500))

        exit_text = font.render("Press Esc to Exit", True, (255, 255, 255))
        self.screen.blit(exit_text, (500, 550))
        pygame.display.flip()

    def center_rect(self, rect_object):
        rect_object.center = (self.width / 2, self.height / 2)