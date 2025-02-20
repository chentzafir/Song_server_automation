import configparser
import os

class Config:
    # Reading the INI file
    _config = configparser.ConfigParser()
    _config_path = os.path.join(os.path.dirname(__file__), '..' , 'resources' ,'config.ini')
    _config.read(_config_path)

    # Reading the values from ini
    HOST = _config['Server']['HOST']