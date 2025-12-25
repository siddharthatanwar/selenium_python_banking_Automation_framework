from apis.base_api import BaseAPI

class UserAPI(BaseAPI):

    def get_users(self, page=1):
        return self.get(f"/api/users?page={page}")

    def create_user(self, name, job):
        payload = {
            "name": name,
            "job": job
        }
        return self.post("/api/users", payload)
