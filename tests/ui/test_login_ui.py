import pytest
from core.base_test import BaseTest
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.smoke
class TestLoginUI(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert "Secure Area" in self.driver.page_source
