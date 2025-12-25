from core.wait_utils import WaitUtils

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
