import Config.config

"""
    TestData folder contains all the test data for test cases 
    (ex:- test cases data/ attachments / images )

    GENERIC_PATH / Config.config.SLASH specifies that common path root for different OS machines

    And segregated the some of the files with json format to right way to use them

"""
""" ---------------------------------------------------------------------------------------------------- 
                                GENERIC PATH TO ALL OF THEM
 ---------------------------------------------------------------------------------------------------- """
GENERIC_PATH = Config.config.COMMON_FOLDER_PATH
CRPO_DATA = 'TestData' + Config.config.SLASH + 'CRPO' + Config.config.SLASH
CRPO_TEST_RESULT = 'Reports' + Config.config.SLASH + 'CRPO' + Config.config.SLASH


""" ---------------------------------------------------------------------------------------------------- 
                                    LOGIN EXCEL PATH
 ---------------------------------------------------------------------------------------------------- """
LOGIN_FILE = {
    'login_credentials': GENERIC_PATH + 'TestData' + Config.config.SLASH + 'LOGIN_DETAILS.xls'
}

""" ---------------------------------------------------------------------------------------------------- 
                                    IMAGE FOLDER
 ---------------------------------------------------------------------------------------------------- """
IMAGE_FILE = {
    'image': GENERIC_PATH + 'ScreenShots' + Config.config.SLASH + '{}.png'
}


""" ---------------------------------------------------------------------------------------------------- 
                                       ATTACHMENTS 
 ---------------------------------------------------------------------------------------------------- """
ATTACHMENT = {
    'job_description': GENERIC_PATH + CRPO_DATA + ''
}


""" ---------------------------------------------------------------------------------------------------- 
                                       INPUT PATHS 
 ---------------------------------------------------------------------------------------------------- """
INPUT = {
    'Mass': GENERIC_PATH + CRPO_DATA + 'Mass_Interview.xls'
}


""" ---------------------------------------------------------------------------------------------------- 
                                       OUTPUT PATHS 
 ---------------------------------------------------------------------------------------------------- """
OUTPUT = {
    'crpo_e2e': GENERIC_PATH + CRPO_TEST_RESULT + 'UI_CRPO_E2E_FLOW.xls'
}
