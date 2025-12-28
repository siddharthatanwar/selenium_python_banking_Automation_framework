from apis.base_api import BaseAPI
from core.config_reader import ConfigReader

class UserAPI(BaseAPI):

    def __init__(self):
        base_url = ConfigReader.get_env("api")["users_base_url"]
        super().__init__(base_url)

    def get_users(self, page=1):
        # DummyJSON paginates as skip/limit
        skip = (page - 1) * 10
        return self.get(f"/users?limit=10&skip={skip}")

    def create_user(self, name, job):
        payload = {
            "firstName": name,
            "company": job
        }
        return self.post("/users/add", payload)
