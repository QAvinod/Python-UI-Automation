import WebdriverWait
from logger_settings import ui_logger
from PageObjects import page_elements
from selenium.webdriver.common.by import By


def button(self, button_name):
    try:
        WebdriverWait.DriverWait.presence_element(self,
                                                  By.XPATH,
                                                  page_elements.BUTTON['button'].format(button_name))
        self.web_element_by_locator.click()
    except Exception as error:
        ui_logger(error)
