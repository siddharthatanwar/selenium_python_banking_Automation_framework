import pytest
from apis.user_api import UserAPI
from apis.payment_api import PaymentAPI


@pytest.fixture(scope="class")
def user_api():
    return UserAPI()


@pytest.fixture(scope="class")
def payment_api():
    return PaymentAPI()
