import logging
import logging.config
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        logging.config.fileConfig("app/resources/logback.conf")
        self.logger = logging.getLogger(logger)


    def getlog(self):
        return self.logger
