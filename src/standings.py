import datasource


def get():
    print "Looking for environment variable MATCH_DATA for data store..."
    try:
        DATA_STORE_URL = environ['MATCH_DATA']
        print "found match data location!"
    except:
        print "WARNING! Failed to find a MATCH_DATA URL! Will not be able to get data!"

    match_slips = DataSource(DATA_STORE_URL).get_match_slips()
    return calculate_points(match_slips)


def calculate_points(match_slips):
    """takes a list of MatchRecords"""
    print "Calcuating points!"
    records = setup_empty_standings(match_slips)
    flatten_matches(match_slips, records)
    standings = []
    for player in records:
        print "Found " + str(len(records)) + " players"
        points = 0

        opponents = set([])
        wins = 0
        played = 0
        for match in records[player]:
            played += 1
            opponents.add(match.opponent)
            if match.won:
                points +=3
                wins += 1
            else:
                points += 1
        uniquePlayerPoints = 2 * len(opponents)
        points += uniquePlayerPoints
        print player + " has played " + str(len(opponents)) + " unique opponents"
        standings.append((player, points, played, wins, played - wins, formatSet(opponents)))

    return sorted(standings, reverse=True, key=lambda tup: tup[1])

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
