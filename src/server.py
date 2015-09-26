import argparse

from os import environ
from flask import Flask
from flask import render_template
import standings
from datasource import DataSource

app = Flask(__name__)


@app.route("/")
def hello():
    return get_standings()

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/standings")
def get_standings():
    match_slips = get_datasource().get_match_slips()
    results = standings.calculate_points(match_slips)
    return render_template("standings.html", standings=results)

def get_datasource():
    print "Looking for environment variable MATCH_DATA"
    try:
        DATA_STORE_URL = environ['MATCH_DATA']
        print "found match data location of " + DATA_STORE_URL
        return DataSource(DATA_STORE_URL)
    except Exception, e:
        print "Failed to find a MATCH_DATA URL! Will not be able to get data!"
        print e

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default="5000")
parser.add_argument('--ip', default="127.0.0.1")
parser.add_argument('--debug', default=False)
args = parser.parse_args()

if __name__ == "__main__":
    app.run(
        host=args.ip,
        debug=args.debug,
        port=args.port,
    )
