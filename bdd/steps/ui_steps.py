import pytest
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

pytestmark = pytest.mark.ui

scenarios("../features/ui/login.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@given("user is on login page")
def open_login_page(login_page):
    login_page.open()


@when("user logs in with valid credentials")
def login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")


@then("user should see secure area page")
def verify_login(driver):
    
    assert "Secure Area" in driver.page_source
