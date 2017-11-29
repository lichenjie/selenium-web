import configparser

class ConfigParse():
    def __init__(self):
        self.config = configparser.ConfigParser()
        file_path = 'app/resources/config.conf'
        self.config.read(file_path)

    def getconfig(self):
        return self.config


