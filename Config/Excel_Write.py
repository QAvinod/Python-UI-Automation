import xlwt
import datetime
from Config import styles
from datetime import date
from logger_settings import ui_logger


class ExcelReport(styles.FontColor):
    """
    Excel write to compare the actual and expected data to make PASS / FAIL status.

        :Notes:
        - excel_write_headers :: Parameterised method to write testcase headers in excel.

        - overall_status :: Parameterised method to write overall details in main headers
                            in the excel(usecase name / overall testcases status / server / version ...etc.)

        - write_actual_test_data :: Write actual testcase data in excel to verify the expected data by view.

        - write_expected_test_data :: Compare actual and expected data and success data as PASS in excel.

    """

    def __init__(self):
        self.date_now = str(date.today())
        self.Expected_success_cases = []
        self.Actual_success_cases = []

        super(ExcelReport, self).__init__()

    def excel_write_headers(self, excel_sheet_name, excel_headers, excel_headers_style_0, no_of_test_cases):

        """ ------------------------------------------------------------------------------------------------
                                    Excel sheet write for Output results
        ---------------------------------------------------------------------------------------------------"""
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, no_of_test_cases)))

        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(excel_sheet_name))

        index = 0
        excelheaders = excel_headers
        for headers in excelheaders:
            if headers in excel_headers_style_0:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def overall_status(self, usecase_start_date_time, usecase_name,
                       version_name_to_print,
                       server_name, output_file_path):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - usecase_start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, usecase_name, self.style4)
            if self.Expected_success_cases == self.Actual_success_cases:
                self.ws.write(0, 1, 'Pass', self.style5)
            else:
                self.ws.write(0, 1, 'Fail', self.style6)

            self.ws.write(0, 2, 'SPRINT VERSION', self.style4)
            self.ws.write(0, 3, 'Sprint_{}'.format(version_name_to_print), self.style5)
            self.ws.write(0, 4, 'SPRINT DATE', self.style4)
            self.ws.write(0, 5, self.date_now, self.style5)
            self.ws.write(0, 6, 'SERVER', self.style4)
            self.ws.write(0, 7, server_name, self.style5)
            self.ws.write(0, 8, 'Success Cases', self.style4)
            self.ws.write(0, 9, len(self.Actual_success_cases), self.style5)
            self.ws.write(0, 10, 'Failure Cases', self.style4)
            if failure_cases == 0:
                self.ws.write(0, 11, failure_cases, self.style5)
            else:
                self.ws.write(0, 11, failure_cases, self.style6)
            self.ws.write(0, 12, 'Success %', self.style4)
            self.ws.write(0, 13, percentage, self.style5)
            self.ws.write(0, 14, 'Time Taken (min)', self.style4)
            self.ws.write(0, 15, minutes, self.style5)
            self.wb_Result.save(output_file_path)

        except Exception as error:
            ui_logger.error(error)

    def write_actual_test_data(self, row, col, test_case):
        try:
            self.ws.write(row, col, test_case, self.style8)

        except Exception as error:
            ui_logger.error(error)

    def write_expected_test_data(self, row, col, test_case, output_file_path):
        try:
            if test_case == 'Pass':
                self.Actual_success_cases.append(test_case)
                self.ws.write(row, col, 'Pass', self.style7)
            else:
                self.ws.write(row, col, 'Fail', self.style3)

            self.wb_Result.save(output_file_path)

        except Exception as error:
            ui_logger.error(error)
