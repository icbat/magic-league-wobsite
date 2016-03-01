from config import Config
import os.path

config_file = "./src/tests/test-config.ini"

def test_defaults():
    config = Config()

    assert(config.points_per_win() == 3)
    assert(config.points_per_loss() == 1)
    assert(config.points_per_unique_opponent() == 2)

def test_defaults_can_be_overidden():
    config = Config()

    config.parse(config_file)

    assert(config.points_per_win() == 5)
    assert(config.points_per_loss() == 6)
    assert(config.points_per_unique_opponent() == 7)

def test_file_not_found_handled():
    config = Config()

    config.parse("some bad file")
    assert(config.points_per_win() == 3)

def test_malformed_file():
    config = Config()

    config.parse("./src/tests/test-bad-config.ini")
    "./src/tests/test-config.ini"
