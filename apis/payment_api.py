from apis.base_api import BaseAPI

class PaymentAPI(BaseAPI):

    def get_products(self):
        return self.get("/products")

    def get_single_product(self, product_id):
        return self.get(f"/products/{product_id}")
