def get():
    # get data
    # then work on it
    return calculateStandings()

"""takes a list of MatchRecords"""
def calculateStandings(matches):
    standings = setupEmptyStandings(matches)
    for match in matches:
        reporterPoints = 0
        opponentPoints = 0
        if (wonMatch(match.reporter, match)):
            reporterPoints = 3
            opponentPoints = 1
        else:
            reporterPoints = 1
            opponentPoints = 3

        reporterOld = standings[match.reporter]

        standings[match.reporter] = reporterOld + reporterPoints

        opponentOld = standings[match.opponent]

        standings[match.opponent] = opponentOld + opponentPoints



    return standings

def setupEmptyStandings(matches):
    players = set([])

    for match in matches:
        players.add(match.reporter)
        players.add(match.opponent)

    playerRecords = {}

    for player in players:
        playerRecords[player] = 0

    return playerRecords

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
