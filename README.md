# magic-league-wobsite
A magic league website with standings driven by spreadsheet

## Running it live

This is currently deployed on Heroku. The Procfile defines what runs in that case.

The match history is backed by Google Docs.

### Environment Variables

This application needs two environment variables to run:

* MATCH_DATA - a URL to a google docs spreadsheet backing match reports. Parsing is currently tightly coupled to that =)

### Arguments

The server app takes a few command-line arguments:

* --port <an int (default:5000)> - sets the port for the mcSlack server to run on. Used by Heroku to allow dynamic port allocation
* --ip <an int (default:127.0.0.1)> - sets the IP to listen on. Allows Heroku to dynamically set this on deploy. Setting to 0.0.0.0 listens to any IP.
* --debug <True or False, defaults to False> - If True, every change to the application's source files will force a live reload of the server. Useful for development, never use this in production.

## Installation

1. Clone the repository
2. Install python 2.7.x and virtualenv
3. Navigate to the directory cloned
4. Run `virtualenv .` to set up virtualenv
5. Activate the new virtual environment with `Scripts/activate.bat` (or the linux equivalent)
6. Run `pip install -r requirements.txt` to install necessary dependencies
7. Run the server with `python src/server.py`
