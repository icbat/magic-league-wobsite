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

def test_countWins():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculateStandings(results)

    assert(standings["lsv"] == 1)
    assert(standings["finkel"] == 3)

def ignore_multipleMatches_getsPoints():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
        ]

    standings = calculateStandings(results)

    assert(standings["lsv"] == 4)
    assert(standings["finkel"] == 4)
