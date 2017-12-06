from selenium import webdriver
from app.core import config_parser
from app.core import logging
import platform
from pyvirtualdisplay import Display


logger = logging.Logger(__name__).getlog()


class BrowserEngine(object):
    config = config_parser.ConfigParse().getconfig()

    def __init__(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        browser = self.config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)

        logger.info("platform.system():%s" % platform.system())
        if browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=self.config.get("driver", "linux_firefox_driver_path"))
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=self.config.get("driver", "linux_chrome_driver_path"))
            logger.info("Starting Chrome browser.")


    # read the browser type from config.properties file, return the driver
    def open_browser(self):
        url = self.config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

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
        self.display.stop()




