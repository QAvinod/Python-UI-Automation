def excel_write(self):
    headers = ['a', 'b', 'c', 'd']
    header_style_0 = ['b', 'd']
    self.excel_write_headers('dummy', headers, header_style_0, no_of_test_cases=3)

    self.write_actual_test_data(2, 0, self.xl_tenant_crpo)
    self.write_actual_test_data(3, 0, self.xl_user_name)
    self.write_actual_test_data(4, 0, self.xl_password_crpo)
    self.write_expected_test_data(2, 1, 'Pass', file_paths.OUTPUT['crpo_e2e'])
    self.write_expected_test_data(3, 1, 'Pass', file_paths.OUTPUT['crpo_e2e'])
    self.write_expected_test_data(4, 1, 'Pass', file_paths.OUTPUT['crpo_e2e'])

    self.overall_status(self.start_date_time, 'first', 137, 'amsin', file_paths.OUTPUT['crpo_e2e'])

