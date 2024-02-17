def show_game_over_screen(screen, pygame, score, high_score):
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
    return score, high_score
