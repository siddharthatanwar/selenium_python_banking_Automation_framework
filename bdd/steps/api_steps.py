import pytest
from pytest_bdd import scenarios, when, then
from apis.user_api import UserAPI


scenarios("../features/api/get_users.feature")


@pytest.fixture
def user_api():
    return UserAPI()


@when("I call get users API")
def call_users_api(user_api):
    response = user_api.get_users(page=1)
    pytest.api_response = response


@then("API should return status 200")
def verify_status():
    assert pytest.api_response.status_code == 200


@then("response should contain user data")
def verify_data():
    assert "users" in pytest.api_response.json()
