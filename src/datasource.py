from os import environ
import requests

print "Looking for environment variable MATCH_DATA for data store..."
DATA_STORE_URL = environ['MATCH_DATA']
print "found match data location!"

def get_match_slips():
    page = requests.get(DATA_STORE_URL)
    html = page.content
    html = html.split("<tbody>")[1]
    html = html.split("</tbody>")[0]
    print html

get_match_slips()
