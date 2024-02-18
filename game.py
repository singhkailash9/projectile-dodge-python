class Game:
    def __init__(self):
        self.running = True
        self.game_over = False

    def reset_game(self, score):
        score.score = 0
        self.game_over = False
