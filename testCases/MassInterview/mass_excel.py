from Config import file_paths, Excel_Read
from utilities import ExcelData


class MassExcel(Excel_Read.ExcelRead):
    def __init__(self):
        self.server_name = 'amsin'

        super(MassExcel, self).__init__()
        self.Login_details_path = file_paths.INPUT['Mass']

        # ------------------ Excel Data Initialization -------------------------------
        ExcelData.excel_data(self, self.Login_details_path)

        self.xl_event_name_m = self.excel_dict['Event_name'][0]
        self.xl_stage_m = self.excel_dict['Slot_team_Size'][0]
        self.xl_size_m = self.excel_dict['Mass_Stage'][0]
        self.xl_status_m = self.excel_dict['Mass_status'][0]
        self.xl_comment_m = self.excel_dict['Comment'][0]
        self.xl_int1_name = self.excel_dict['Int1_name'][0]
        self.xl_int1_user = self.excel_dict['int1'][0]
        self.xl_int1_pwd = self.excel_dict['int1_pwd'][0]
        self.xl_int2_name = self.excel_dict['Int2_name'][0]
        self.xl_int2_user = self.excel_dict['int2'][0]
        self.xl_int2_pwd = self.excel_dict['int2_pwd'][0]
        self.xl_to_be_Queued = self.excel_dict['be_Queued'][0]
        self.xl_interview_pending = self.excel_dict['Interview_Pending'][0]
        self.xl_awaited = self.excel_dict['awaited'][0]
        self.xl_shortlist_m = self.excel_dict['shortlist'][0]
        self.xl_message_m = self.excel_dict['Message'][0]


o = MassExcel()