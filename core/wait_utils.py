from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from core.config_reader import get_wait_config   # 👈 YOUR file

wait_config = get_wait_config()

DEFAULT_TIMEOUT = float(wait_config["timeout"])
DEFAULT_POLL = float(wait_config["poll"])

logger = logging.getLogger("AutomationLogger")

class WaitUtils:

    def __init__(self, driver, timeout=20):
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
