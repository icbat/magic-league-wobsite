def calculate_points(match_slips, config):
    """takes a list of MatchRecords"""
    print "Calcuating points!"
    records = setup_empty_standings(match_slips)
    flatten_matches(match_slips, records)
    standings = []
    print "Found " + str(len(records)) + " players"
    for player in records:
        player_records = records[player]

        matches_played = count_matches(player_records)
        opponents = find_unique_opponents(player_records)
        wins = count_wins(player_records)

        points = calculate_match_points(player_records, config)
        uniquePlayerPoints = config.points_per_unique_opponent() * len(opponents)
        points += uniquePlayerPoints

        print player + " has played " + str(len(opponents)) + " unique opponents"
        standings.append((player, points, matches_played, wins, matches_played - wins, formatSet(opponents)))

    return sorted(standings, reverse=True, key=lambda tup: tup[1])

def count_matches(records):
    return len(records)

def find_unique_opponents(records):
    opponents = set([])
    for match in records:
        opponents.add(match.opponent)
    return opponents

def count_wins(records):
    wins = 0
    for match in records:
        if match.won:
            wins += 1
    return wins

def calculate_match_points(records, config):
    points = 0
    for match in records:
        if match.won:
            points += config.points_per_win()
        else:
            points += config.points_per_loss()
    return points

def formatSet(aSet):
    return ", ".join(aSet)

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
