import page_elements
import image_capture
from logger_settings import ui_logger
from selenium.webdriver.common.by import By


def connection_error(self):
    # ----------------------------------------- Server Connection error --------------------------------------------
    try:
        unable_to_reach_server = self.driver.find_element(By.XPATH,
                                                          page_elements.LOGIN['page_cant_be_reached'])
        try:
            assert 'This site' in unable_to_reach_server.text
            image_capture.screen_shot(self, 'server connection failed')
            print("Server connection has been lost and screen shot saved")
        except Exception as error:
            ui_logger.error(error)
    except Exception as error1:
        ui_logger.error(error1)
