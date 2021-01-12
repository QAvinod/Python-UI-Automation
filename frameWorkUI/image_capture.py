from Config import file_paths
from logger_settings import ui_logger


def screen_shot(self, image_name):
    try:
        self.driver.save_screenshot(file_paths.IMAGE_FILE['image'].format(image_name))
    except Exception as image_error:
        ui_logger.error(image_error)
