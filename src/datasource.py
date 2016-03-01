import requests
from match import MatchRecord

class DataSource:
    def __init__(self, DATA_STORE_URL):
        self.DATA_STORE_URL = DATA_STORE_URL

    def parse_match_slips(self, raw_match_slips):
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


    def get_match_slips(self):
        raw_match_slips = self.get_raw_match_slips()
        return self.parse_match_slips(raw_match_slips)


    def get_raw_match_slips(self):
        print "Getting match slips from " + self.DATA_STORE_URL
        page = requests.get(self.DATA_STORE_URL)
        html = page.content
        html = html.split("<tbody>")[1]
        html = html.split("</tbody>")[0]
        split = html.split("</tr>")
        return split
