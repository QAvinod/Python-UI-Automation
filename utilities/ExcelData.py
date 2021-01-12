from logger_settings import ui_logger


def excel_data(self, file_path):
    try:
        self.LOGIN_DETAILS = file_path

        if self.server_name == 'amsin':
            self.read(self.LOGIN_DETAILS, index=0)
        if self.server_name == 'ams':
            self.read(self.LOGIN_DETAILS, index=1)

    except Exception as error:
        ui_logger(error)
