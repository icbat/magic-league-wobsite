import datasource


def test_getMatchSlips_noURL():
    try:
        datasource.get_match_slips()
        # Undefined behavior, should fail
        assert(False)
    except:
        assert(True)


def test_parsing_notEnoughData_returnsEmpty():
    row = ""
    raw_rows = [row]
    slips = datasource.parse_match_slips(raw_rows)

    assert(len(slips) == 0)


def test_parsing_oneRow():
    row = "<td>a</td><td>b</td><td>c</td><td>d</td><td>e</td>"
    raw_rows = [row]
    slips = datasource.parse_match_slips(raw_rows)

    assert(len(slips) == 1)


def test_parsing_oneRow_missingColumnWontRecord():
    row = "<td></td><td>b</td><td>c</td><td>d</td><td>e</td>"
    raw_rows = [row]
    slips = datasource.parse_match_slips(raw_rows)

    assert(len(slips) == 0)
