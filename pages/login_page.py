from selenium.webdriver.common.by import By
from core.base_page import BasePage
from core.config_reader import ConfigReader
import logging

class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        base_url = ConfigReader.get_env("app")["base_url"]
        logging.getLogger("AutomationLogger").info("Opening login page")
        logging.getLogger("AutomationLogger").info("LoginPage.open() called")
        self.driver.get(base_url + "/login")

    def login(self, username, password):
        self.wait.wait_for_visibility(self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
