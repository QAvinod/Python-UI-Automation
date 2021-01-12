import image_capture
from logger_settings import ui_logger
from frameWorkUI import WebdriverWait


class Element(WebdriverWait.DriverWait):
    def __init__(self):
        super(Element, self).__init__()
        self.element_text = ''

    def send_keys(self, by_locator, element, value):
        try:
            self.presence_element(by_locator, element)
            self.web_element_by_locator.send_keys(value)
        except Exception as error:
            ui_logger(error)

    def text(self, by_locator, element, text_value):
        try:
            self.presence_element(by_locator, element)
            self.element_text = self.web_element_by_locator.text
            if self.element_text.strip() == text_value:
                print('**--------------> Validation check verified')
            else:
                image_capture.screen_shot(self, text_value)
        except Exception as error:
            ui_logger(error)

        return self.element_text.strip()

    def click(self, by_locator, element):
        try:
            self.presence_element(by_locator, element)
            self.web_element_by_locator.click()
        except Exception as error:
            ui_logger(error)
