def get():
    # get data
    # then work on it
    return calculateStandings()

"""takes a list of MatchRecords"""
def calculateStandings(matches):
    standings = setupEmptyStandings(matches)

    return standings

def setupEmptyStandings(matches):
    players = set([])

    for match in matches:
        players.add(match.reporter)
        players.add(match.opponent)

    standings = set([])

    for player in players:
        standings.add(Player(player))

    return standings

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
