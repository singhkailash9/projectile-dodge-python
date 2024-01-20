import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 690))
clock = pygame.time.Clock()
running = True
dt = 0

screen_width = screen.get_width()
screen_height = screen.get_height()
player_rect = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)

projectiles = []

score = 0
high_score = 0

game_over = False

def show_game_over_screen():
    global score, high_score, game_over
    game_over = True
    if score > high_score:
        high_score = score

    screen.fill("black")
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (450, 300))

    font = pygame.font.Font(None, 36)
    final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(final_score_text, (500, 400))

    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    screen.blit(high_score_text, (500, 450))

    retry_text = font.render("Press R to Retry", True, (255, 255, 255))
    screen.blit(retry_text, (500, 500))

    exit_text = font.render("Press Esc to Exit", True, (255, 255, 255))
    screen.blit(exit_text, (500, 550))

    pygame.display.flip()

def reset_game():
    global score, game_over
    score = 0
    game_over = False
    player_rect.center = (screen_width / 2, screen_height / 2)
    projectiles.clear()

class Projectile:
    def __init__(self, x, y, speed):
        self.speed = speed
        self.rect = pygame.Rect(x, y, 10, 10)

    def move(self):
        self.rect.move_ip(0, self.speed)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        show_game_over_screen()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Retry
                    reset_game()
                elif event.key == pygame.K_ESCAPE:  # Quit
                    pygame.quit()
                    sys.exit()
    else:
        screen.fill("purple")

        pygame.draw.rect(screen, "red", player_rect)

        keys = pygame.key.get_pressed()
        move_distance = 300 * dt
        if keys[pygame.K_w]:
            player_rect.y -= move_distance
        if keys[pygame.K_s]:
            player_rect.y += move_distance
        if keys[pygame.K_a]:
            player_rect.x -= move_distance
        if keys[pygame.K_d]:
            player_rect.x += move_distance
        if keys[pygame.K_SPACE]:
            player_rect.y -= 1.5 * move_distance

        if pygame.time.get_ticks() % 2 == 0:
            next_projectile = random.randint(2, screen_width)
            new_projectile = Projectile(next_projectile, 0, 3)
            projectiles.append(new_projectile)
            score += 1

        for projectile in projectiles:
            projectile.move()
            pygame.draw.rect(screen, "white", projectile.rect)

            # Check for collisions between the player and projectiles
            if player_rect.colliderect(projectile.rect):
                show_game_over_screen()

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        dt = clock.tick(60) / 1000

pygame.quit()
