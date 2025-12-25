from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            options = Options()
            options.add_argument("--start-maximized")

            driver_path = os.path.join(
                os.getcwd(), "drivers", "chromedriver.exe"
            )

            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)
            return driver

        else:
            raise Exception("Browser not supported")
