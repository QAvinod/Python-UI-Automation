import Environment
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DriverWait(Environment.Environment):
    """ Generic function will be easy to do script writing.
    """
    def __init__(self):
        super(DriverWait, self).__init__()
        self.wait = WebDriverWait(self.driver, 10)
        self.web_element_by_locator = ''

    def driver_wait(self):
        self.wait = WebDriverWait(self.driver, 10)

    def clickable_element(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.element_to_be_clickable((by_locator, element)))

    def visibility_element(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.visibility_of_element_located((by_locator, element)))

    def visibility_elements(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.visibility_of_all_elements_located((by_locator, element)))

    def visibility_any_elements(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.visibility_of_any_elements_located((by_locator, element)))

    def presence_element(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.presence_of_element_located((by_locator, element)))

    def presence_elements(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.presence_of_all_elements_located((by_locator, element)))

    def text_elements(self, by_locator, element):
        self.web_element_by_locator = self.wait.until(ec.text_to_be_present_in_element((by_locator, element), ''))


