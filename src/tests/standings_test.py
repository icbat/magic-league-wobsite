from standings import calculatePoints, wonMatch, flattenMatches
from match import MatchRecord

def test_noMatches():
    standings = calculatePoints([])

    assert(len(standings) == 0)

def test_oneMatch_getsReported():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculatePoints(results)

    assert(len(standings) == 2)

def test_multipleMatches_dontCreateDuplicates():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
        ]

    standings = calculatePoints(results)

    assert(len(standings) == 2)

def test_countWins():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculatePoints(results)

    assert(standings["lsv"] == 3)
    assert(standings["finkel"] == 5)

def test_multipleMatches_getsPoints():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
        ]

    standings = calculatePoints(results)

    assert(standings["lsv"] == 6)
    assert(standings["finkel"] == 6)

def test_multipleOpponents_countedCorrectly():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "pv", 0),
    ]


    standings = calculatePoints(results)

    assert(standings["lsv"] == 8)

def test_winLoss():
    match = MatchRecord("lsv", 1, "finkel", 2)

    assert(wonMatch("finkel", match) == True)
    assert(wonMatch("lsv", match) == False)
    assert(wonMatch("frankerz", match) == False)

def test_flatten():
    matches = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
        ]

    records = {"lsv" : [], "finkel" : []}
    assert(len(records["lsv"]) == 0)
    assert(len(records["finkel"]) == 0)

    flattenMatches(matches, records)

    assert(len(records) == 2)
    assert(len(records["lsv"]) == 2)
    assert(len(records["finkel"]) == 2)
