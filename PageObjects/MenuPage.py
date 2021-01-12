from utilities import MenuTabs
from logger_settings import ui_logger

TAB = {

}


def event(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='Events')
    except Exception as error:
        ui_logger.error(error)


def job(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='Job Roles')
    except Exception as error:
        ui_logger.error(error)


def requirement(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='Requirements')
    except Exception as error:
        ui_logger.error(error)


def assessment(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='Assessments')
    except Exception as error:
        ui_logger.error(error)


def candidates(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='Candidates')
    except Exception as error:
        ui_logger.error(error)


def more(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='More')
    except Exception as error:
        ui_logger.error(error)


def settings(self):
    try:
        MenuTabs.menu_tabs(self, tab_name='administrator')
    except Exception as error:
        ui_logger.error(error)
