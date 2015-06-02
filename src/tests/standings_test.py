from standings import calculateStandings
from match import MatchRecord

def test_noMatches():
    standings = calculateStandings([])

    assert(len(standings) == 0)

def test_oneMatch_getsReported():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculateStandings(results)

    assert(len(standings) == 2)

def test_multipleMatches_dontCreateDuplicates():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
        ]

    standings = calculateStandings(results)

    assert(len(standings) == 2)

def test_winsAreCounted():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculateStandings(results)

    for player in standings:
        if (player.name == "lsv"):
            assert(player.wins == 1)
        elif (player.name == "finkel"):
            assert(player.wins == 2)
        else:
            assert(False)
