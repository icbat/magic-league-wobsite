def get():
    # get data
    # then work on it
    return calculateStandings()

"""takes a list of MatchRecords"""
def calculateStandings(matches):
    standings = setupEmptyStandings(matches)
    for match in matches:
        reporterOld = standings[match.reporter]

        standings[match.reporter] = reporterOld + 1

        opponentOld = standings[match.opponent]

        standings[match.opponent] = opponentOld + 3



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
