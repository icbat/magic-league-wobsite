from os import environ
import requests
from match import MatchRecord

print "Looking for environment variable MATCH_DATA for data store..."
DATA_STORE_URL = environ['MATCH_DATA']
print "found match data location!"


def parse_match_slips(raw_match_slips):
    slips = []
    for slip in raw_match_slips:
        fields = slip.split("</td>")
        slipFields = []
        for field in fields:
            parsed = field.split(">")[-1]
            if len(parsed) > 0:
                slipFields.append(parsed)

        if len(slipFields) == 5:
            reporter = slipFields[1]
            wins = slipFields[2]
            opponent = slipFields[3]
            losses= slipFields[4]
            slips.append(MatchRecord(reporter, wins, opponent, losses))

    return slips

def get_match_slips():
    raw_match_slips = get_raw_match_slips()
    return parse_match_slips(raw_match_slips)

def get_raw_match_slips():
    page = requests.get(DATA_STORE_URL)
    html = page.content
    html = html.split("<tbody>")[1]
    html = html.split("</tbody>")[0]
    split = html.split("</tr>")
    return split
