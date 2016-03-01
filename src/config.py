import ConfigParser
import os.path

class Config:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.pointsPerWin = 3
        self.pointsPerLoss = 1
        self.pointsPerUniqueOpponent = 2

    def parse(self, filename):
        if os.path.isfile(filename):
            self.config.read(filename)
            self.pointsPerWin = self.get_property("Points", "points_per_win")
            self.pointsPerLoss = self.get_property("Points", "points_per_loss")
            self.pointsPerUniqueOpponent = self.get_property("Points", "points_per_unique_opponent")
        else:
            print "Couldn't find or read file at: " + filename
            print "Using default values"

    def get_property(self, section, propName):
        try:
            return int(self.config.get(section, propName))
        except:
            print "Couldn't parse property " + propName + " in section " + section


    def points_per_win(self):
        return self.pointsPerWin

    def points_per_loss(self):
        return self.pointsPerLoss

    def points_per_unique_opponent(self):
        return self.pointsPerUniqueOpponent
