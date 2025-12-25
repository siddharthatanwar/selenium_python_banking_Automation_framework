import pytest
import logging
from core.driver_factory import DriverFactory

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request):
        self.logger = logging.getLogger("AutomationLogger")

        browser = request.config.getoption("--browser")
        self.logger.info(f"Starting browser: {browser}")

        self.driver = DriverFactory.get_driver(browser)
        yield
        self.logger.info("Closing browser")
        self.driver.quit()
