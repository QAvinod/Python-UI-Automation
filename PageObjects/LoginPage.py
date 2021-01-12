from PageObjects import page_elements
from frameWorkUI.logger_settings import ui_logger
from selenium.webdriver.common.by import By
from utilities import ButtonClick, ExplicitWait, NoElementFound

LOGIN = {
    'alias': 'alias',
    'login_name': 'loginName',
    'password': '//input[@type="password"]',
    'login': '.button_style',
    'login_page_validation': 'login_style',
    'login_success': '/html/body/div[1]/div/header/div[1]/nav/div/div[3]/ul/li/a',
}


class LoginPage:

    @staticmethod
    def app_title(self, app_name):
        try:
            if self.driver.title == app_name:  # ----------- Based on TITLE validate and continuing
                pass
        except Exception as login_error:
            ui_logger.error(login_error)
            return False
        return True

    @staticmethod
    def tenant_value(self, tenant_name):
        try:
            ExplicitWait.Element.send_keys(self, By.NAME, LOGIN['alias'], tenant_name)
        except Exception as login_error:
            ui_logger.error(login_error)

    @staticmethod
    def next_to(self):
        try:
            ButtonClick.button(self, 'Next')
        except Exception as login_error:
            ui_logger.error(login_error)

    @staticmethod
    def username_value(self, user_name):
        try:
            ExplicitWait.Element.send_keys(self, By.NAME, LOGIN['login_name'], user_name)
        except Exception as login_error:
            ui_logger.error(login_error)

    @staticmethod
    def password_value(self, password_name):
        try:
            ExplicitWait.Element.send_keys(self, By.XPATH, LOGIN['password'], password_name)
        except Exception as login_error:
            ui_logger.error(login_error)

    @staticmethod
    def do_login(self):
        try:
            ExplicitWait.Element.click(self, By.CSS_SELECTOR, LOGIN['login'])
        except Exception as login_error:
            ui_logger.error(login_error)

    @staticmethod
    def login_page_validation(self, validate_string):
        try:
            assert self.text(By.CLASS_NAME, page_elements.LOGIN['login_page_validation'],
                             validate_string) == validate_string
            print('**--------------> Tenant screen validated and landed into the login screen')
        except Exception as login_error:
            ui_logger.error(login_error)

    @staticmethod
    def login_validation(self):
        # ---------------------------------------- Assertion for login -------------------------------------------------
        try:
            if NoElementFound.check_exists_element(self, By.CSS_SELECTOR, page_elements.NOTIFIER['notifier']):
                print("**-------------->> Login Failed")
                print(self.driver.find_element(By.CSS_SELECTOR, page_elements.NOTIFIER['notifier']).text)

            else:
                self.text(By.XPATH, LOGIN['login_success'], 'administrator')
                if self.element_text.strip() == 'administrator':
                    print("**-------------->> Login Successfully")
                    print("**---------------------- In main Menu screen ------------------------**")

        except Exception as login_status:
            ui_logger.error(login_status)
