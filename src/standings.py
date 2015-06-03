import datasource

def get():
    matchSlips = datasource.getMatchSlips()
    return calculatePoints(matchSlips)

"""takes a list of MatchRecords"""
def calculatePoints(matchSlips):
    records = setupEmptyStandings(matchSlips)
    flattenMatches(matchSlips, records)
    standings = {}
    for player in records:
        points = 0

        opponents = set([])
        for match in records[player]:
            points = points + (3 if match.won else 1)
            opponents.add(match.opponent)
        points = points + (2 * len(opponents))
        standings[player] = points


    return standings

def setupEmptyStandings(matchSlips):
    standings = {}

    for match in matchSlips:
        standings[match.reporter] = []
        standings[match.opponent] = []
    return standings

def flattenMatches(matchSlips, standings):
    for match in matchSlips:
        standings[match.reporter].append(Match(match.reporter, match))
        standings[match.opponent].append(Match(match.opponent, match))

def wonMatch(name, match):
    wins = 0
    losses = 0
    if (match.reporter == name):
        wins = match.wins
        losses = match.losses
    elif (match.opponent == name):
        wins = match.losses
        losses = match.wins

    return wins > losses



class Match:
    def __init__(self, name, match):
        self.won = wonMatch(name, match)
        self.opponent = match.opponent if match.reporter == name else match.reporter
    def __str__(self):
        return str(self.won) + " against " + self.opponent
