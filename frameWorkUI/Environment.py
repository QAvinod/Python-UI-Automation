import datetime
from selenium import webdriver
from logger_settings import ui_logger
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Environment(object):
    """
    No required to do manual webdriver download and unzipped and placed in executable folder.
    webdriver_manager will take care of it while run time checking the updated version.

        :Notes:
        - Always choosing the chrome browser.

        - Required bases we can change the browser where we want to run the scripts
    """
    def __init__(self):
        # self.login_server = input("Server name :: ")
        # self.sprint_version = input("Enter the current sprint version :: ")
        self.browser = 'chrome'

        try:
            if self.browser == 'chrome':
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                print("Chrome Run started at:: "+str(datetime.datetime.now()))
                print("**--------------------------------------------------------------**")
                self.driver.maximize_window()

            elif self.browser == 'firefox':
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                print("Firefox Run started at:: "+str(datetime.datetime.now()))
                print("**--------------------------------------------------------------**")
                self.driver.maximize_window()

            elif self.browser == 'safari':
                self.driver = webdriver.Safari()
                print("Firefox Run started at:: "+str(datetime.datetime.now()))
                print("**-------------------------------------------------------------**")
                self.driver.maximize_window()
            else:
                print("Pass me the correct browser name")

        except Exception as Environment_Error:
            ui_logger.error(Environment_Error)

    def browser_close(self):
        print("**-------------------------------------------------------------**")
        print("{} Run completed at:: ".format(self.browser) + str(datetime.datetime.now()))
        self.driver.close()
