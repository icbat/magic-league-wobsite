from os import environ
import requests
from match import MatchRecord

print "Looking for environment variable MATCH_DATA for data store..."
try:
    DATA_STORE_URL = environ['MATCH_DATA']
    print "found match data location!"
except:
    print "WARNING! Failed to find a MATCH_DATA URL! Will not be able to get data!"


def parse_match_slips(raw_match_slips):
    print "Parsing match slips. Found " + str(len(raw_match_slips))
    slips = []
    for slip in raw_match_slips:
        fields = slip.split("</td>")
        slip_fields = []
        for field in fields:
            parsed = field.split(">")[-1].strip()
            if len(parsed) > 0:
                slip_fields.append(parsed)

        if len(slip_fields) == 5:
            reporter = slip_fields[1].strip()
            wins = slip_fields[2]
            opponent = slip_fields[3].strip()
            losses = slip_fields[4]
            slips.append(MatchRecord(reporter, wins, opponent, losses))

    return slips


def get_match_slips():
    raw_match_slips = get_raw_match_slips()
    return parse_match_slips(raw_match_slips)


def get_raw_match_slips():
    print "Getting match slips from " + DATA_STORE_URL
    page = requests.get(DATA_STORE_URL)
    html = page.content
    html = html.split("<tbody>")[1]
    html = html.split("</tbody>")[0]
    split = html.split("</tr>")
    return split
