import page_elements
import image_capture
from selenium.webdriver.common.by import By
from logger_settings import ui_logger


def internet_not_available(self):
    # ----------------------------------------- Internet Connection error ------------------------------------------
    try:
        internet_error = self.driver.find_element(By.XPATH, page_elements.LOGIN['internet_error'])
        try:
            assert 'No Internet' in internet_error.text
            image_capture.screen_shot(self, 'No Internet')
            print("No Internet connection and screen shot saved")
        except Exception as error:
            ui_logger.error(error)
    except Exception as error2:
        ui_logger.error(error2)
