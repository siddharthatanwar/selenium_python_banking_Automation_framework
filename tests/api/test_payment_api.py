import pytest
from apis.payment_api import PaymentAPI
from core.assertions import assert_key_in_response

@pytest.mark.api
@pytest.mark.regression
class TestPaymentAPI:

    def test_get_products(self):
        api = PaymentAPI()
        response = api.get_products()

        assert response.status_code == 200
        assert len(response.json()["products"]) > 0

    def test_get_single_product(self):
        api = PaymentAPI()
        response = api.get_single_product(1)

        assert response.status_code == 200
        assert response.json()["id"] == 1
