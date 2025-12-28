from apis.base_api import BaseAPI
from core.config_reader import ConfigReader

class PaymentAPI(BaseAPI):

    def __init__(self):
        base_url = ConfigReader.get_env("api")["payments_base_url"]
        super().__init__(base_url)

    def get_products(self):
        return self.get("/products")

    def get_single_product(self, product_id):
        return self.get(f"/products/{product_id}")
