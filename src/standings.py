import datasource


def get():
    match_slips = datasource.get_match_slips()
    return calculate_points(match_slips)


def calculate_points(match_slips):
    """takes a list of MatchRecords"""
    records = setup_empty_standings(match_slips)
    flatten_matches(match_slips, records)
    standings = {}
    for player in records:
        points = 0

        opponents = set([])
        for match in records[player]:
            points += 3 if match.won else 1
            opponents.add(match.opponent)
        points += 2 * len(opponents)
        standings[player] = points

    return standings


def setup_empty_standings(match_slips):
    standings = {}

    for match in match_slips:
        standings[match.reporter] = []
        standings[match.opponent] = []
    return standings


def flatten_matches(match_slips, standings):
    for match in match_slips:
        standings[match.reporter].append(Match(match.reporter, match))
        standings[match.opponent].append(Match(match.opponent, match))


def won_match(name, match):
    wins = 0
    losses = 0
    if match.reporter == name:
        wins = match.wins
        losses = match.losses
    elif match.opponent == name:
        wins = match.losses
        losses = match.wins

    return wins > losses


class Match:
    def __init__(self, name, match):
        self.won = won_match(name, match)
        self.opponent = match.opponent if match.reporter == name else match.reporter

    def __str__(self):
        return str(self.won) + " against " + self.opponent
