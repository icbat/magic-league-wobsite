class MatchRecord:
    def __init__(self, reporter, wins, opponent, losses):
        self.reporter = reporter
        self.wins = wins
        self.opponent = opponent
        self.losses = losses

    def __str__(self):
        return self.reporter + " played " + self.opponent + " and the record was: " + str(self.wins) + " - " + str(
            self.losses)