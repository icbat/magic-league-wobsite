from os import environ

print "Looking for environment variable MATCH_DATA for data store..."
DATA_STORE = environ['MATCH_DATA']
print "found match data location!"
