# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from app.src.core import logging
from app.src.core import config_parser
logger = logging.Logger(__name__).getlog()


class BrowserEngine(object):
    config = config_parser.ConfigParse().getconfig()

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.properties file, return the driver
    def open_browser(self, driver):
        browser = BrowserEngine.config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = self.config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)
        if "mac":
            if browser == "Firefox":
                self.driver = webdriver.Firefox(executable_path = self.config.get("driver", "mac_firefox_driver_path"))
                logger.info("Starting firefox browser.")
            elif browser == "Chrome":
                self.driver = webdriver.Chrome(executable_path = self.config.get("driver", "mac_chrome_driver_path"))
                logger.info("Starting Chrome browser.")

        self.driver.get(url)
        logger.info("Open url: %s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return self.driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()




