import time
from PageObjects import page_elements
from logger_settings import ui_logger
from selenium.webdriver.common.by import By


def menu_tabs(self, tab_name):
    try:
        list_of_menu = self.driver.find_elements(By.CSS_SELECTOR, page_elements.TAB['menu'])
        for tab in list_of_menu:
            if tab.text.strip() == tab_name:
                tab.click()
                time.sleep(2)
                print('**--------------> Clicked on {} Tab'.format(tab_name))
                break
    except Exception as tab_error:
        ui_logger.error(tab_error)
