import time
import datetime
from PageObjects.LoginPage import LoginPage
from PageObjects import MenuPage
from logger_settings import ui_logger
from Config import file_paths, Excel_Read, config
from utilities import ExplicitWait, ExcelData


class Login(Excel_Read.ExcelRead, ExplicitWait.Element):

    def __init__(self):
        self.server_name = input("Server:: ")

        super(Login, self).__init__()
        self.Login_details_path = file_paths.LOGIN_FILE['login_credentials']
        self.start_date_time = ''
        self.status_of_login = ''

        # ------------------ Excel Data Initialization -------------------------------
        ExcelData.excel_data(self, self.Login_details_path)

        self.xl_user_name = self.excel_dict['Login_Name'][0]
        self.xl_password_crpo = self.excel_dict['C_Password'][0]
        self.xl_tenant_crpo = self.excel_dict['C_Tenant_Name'][0]
        self.xl_login_screen_validation_crpo = self.excel_dict['C_LoginScreenV'][0]
        self.xl_login_failed_message = self.excel_dict['C_LoginFailedMessage'][0]

    def crpo_login(self):
        self.driver.get(config.sever_config['crpo'].format(self.server_name))
        self.start_date_time = datetime.datetime.now()

        try:
            assert LoginPage.app_title(self, 'CRPO')
            print('**--------------> Application Title verified')

            LoginPage.tenant_value(self, self.xl_tenant_crpo)
            LoginPage.next_to(self)
            LoginPage.login_page_validation(self, self.xl_login_screen_validation_crpo)
            LoginPage.username_value(self, self.xl_user_name)
            LoginPage.password_value(self, self.xl_password_crpo)
            LoginPage.do_login(self)
            time.sleep(5)

            LoginPage.login_validation(self)

        except Exception as login_error:
            ui_logger.error(login_error)


o = Login()
o.crpo_login()
