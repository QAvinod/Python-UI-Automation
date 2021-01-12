import time
import WebdriverWait
from logger_settings import ui_logger


class WebElementWait(WebdriverWait.DriverWait):
    """ Generic function will be easy to do script writing.
    """
    def __init__(self):
        super(WebElementWait, self).__init__()
        self.web_element_by_locator = ''

    def web_element_wait(self, by_locator, element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                self.web_element_by_locator = self.driver.find_element(by_locator, element)
                result = True
                break
            except Exception as error:
                ui_logger.error(error)
                time.sleep(2)
            attempts += 1
        print('Number of attempts = {}'.format(attempts))
        return result
