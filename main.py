import pygame, random, sys
from game import Game
from player import Player
from projectile import Projectile
from score import Score
from screen import Screen

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 690
PROJECTILE_SPAWN_RATE = 3
PROJECTILE_SPEED = 3

pygame.init()
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
game = Game()
score_manager = Score()
screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

projectiles = []

high_score = score_manager.high_score

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    if game.game_over:
        score_manager.save_score()
        screen.game_over_screen(score_manager.score, score_manager.high_score)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Retry
                    game.reset_game(score_manager)
                    projectiles.clear()
                    screen.center_rect(player.player_rect)
                elif event.key == pygame.K_ESCAPE:  # Quit
                    pygame.quit()
                    sys.exit()
    else:
        screen.screen.fill("purple")
        screen.screen.blit(player.player_image, player.player_rect)

        keys = pygame.key.get_pressed()
        player.move(keys)

        if pygame.time.get_ticks() % PROJECTILE_SPAWN_RATE == 0:
            next_projectile = random.randint(2, screen.width)
            new_projectile = Projectile(next_projectile, 0, PROJECTILE_SPEED)
            projectiles.append(new_projectile)
            score_manager.score += 1

        for projectile in projectiles:
            projectile.move()
            screen.screen.blit(projectile.projectile_image, projectile.rect)

            # Remove projectile once it's out of the screen
            if projectile.rect.y > screen.height:
                projectiles.remove(projectile)

            # Collision detection between the player and projectiles
            if player.player_rect.colliderect(projectile.rect):
                screen.game_over_screen(score_manager.score, score_manager.high_score)
                game.game_over = True

        # Score display
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score_manager.score}", True, (255, 255, 255))
        screen.screen.blit(score_text, (10, 10))

        pygame.display.flip()

        player.dt = screen.clock.tick(60) / 1000

pygame.quit()
