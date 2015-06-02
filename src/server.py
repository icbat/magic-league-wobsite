import argparse

from flask import Flask
from flask import render_template
import standings
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("landing.html")

@app.route("/standings")
def get_standings():
    results = standings.get()
    return render_template("standings.html", standings=results)


parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default="5000")
parser.add_argument('--ip', default="127.0.0.1")
parser.add_argument('--debug', default=False)
args = parser.parse_args()

if __name__ == "__main__":
    app.run(
    	host = args.ip,
    	debug = args.debug,
    	port = args.port,
    	)
