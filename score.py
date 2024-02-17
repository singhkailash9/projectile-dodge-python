class Score:
    def __init__(self, filepath='highscore.txt'):
        self.filepath = filepath
        self.high_score = self.load_high_score()

    def create_high_score_file(self):
        with open(self.filepath, 'w', encoding='utf-8'):
            return

    def load_high_score(self):
        try:
            with open(self.filepath, 'r') as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            self.create_high_score_file()
            return 0

    def save_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open(self.filepath, 'w') as file:
                file.write(str(score))
