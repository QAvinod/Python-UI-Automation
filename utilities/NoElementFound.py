from selenium.common.exceptions import NoSuchElementException


def check_exists_element(self, by_locator, element):
    try:
        self.driver.find_element(by_locator, element)
    except NoSuchElementException:
        return False
    return True
