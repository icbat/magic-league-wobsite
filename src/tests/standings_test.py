from standings import calculate_points, won_match, flatten_matches
from match import MatchRecord
from config import Config

def test_noMatches():
    standings = calculate_points([], Config())

    assert (len(standings) == 0)


def test_oneMatch_getsReported():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculate_points(results, Config())

    assert (len(standings) == 2)


def test_multipleMatches_dontCreateDuplicates():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
    ]

    standings = calculate_points(results, Config())

    assert (len(standings) == 2)


def test_countWins():
    results = [MatchRecord("lsv", 1, "finkel", 2)]

    standings = calculate_points(results, Config())

    assert (find_points_by_name("lsv", standings) == 3)
    assert (find_points_by_name("finkel", standings) == 5)


def test_multipleMatches_getsPoints():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
    ]

    standings = calculate_points(results, Config())

    assert (find_points_by_name("lsv", standings) == 6)
    assert (find_points_by_name("finkel", standings) == 6)


def test_multipleOpponents_countedCorrectly():
    results = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "pv", 0),
    ]

    standings = calculate_points(results, Config())

    assert (find_points_by_name("lsv", standings) == 8)


def test_winLoss():
    match = MatchRecord("lsv", 1, "finkel", 2)

    assert (won_match("finkel", match) == True)
    assert (won_match("lsv", match) == False)
    assert (won_match("frankerz", match) == False)


def test_flatten():
    matches = [
        MatchRecord("lsv", 1, "finkel", 2),
        MatchRecord("lsv", 2, "finkel", 0),
    ]

    records = {"lsv": [], "finkel": []}
    assert (len(records["lsv"]) == 0)
    assert (len(records["finkel"]) == 0)

    flatten_matches(matches, records)

    assert (len(records) == 2)
    assert (len(records["lsv"]) == 2)
    assert (len(records["finkel"]) == 2)


def find_points_by_name(player_name, standings):
    for standing in standings:
        if standing[0] == player_name:
            return standing[1]
    return -1
