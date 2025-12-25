import pytest
from apis.user_api import UserAPI

@pytest.mark.api
class TestUserAPI:

    def test_get_users(self):
        api = UserAPI()
        response = api.get_users(page=2)

        assert response.status_code == 200
        data = response.json()

        assert "data" in data
        assert len(data["data"]) > 0

    def test_create_user(self):
        api = UserAPI()
        response = api.create_user("Siddharth", "QA Architect")

        assert response.status_code == 201
        assert response.json()["name"] == "Siddharth"
