def get():
    # get data
    # then work on it
    return calculateStandings()

"""takes a list of MatchRecords"""
def calculateStandings(matches):
    standings = []

    for player in findPlayers(matches):
        standings.append(Player(player))

    return standings

def findPlayers(matches):
    players = set([])

    for match in matches:
        players.add(match.reporter)
        players.add(match.opponent)
    return players

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
