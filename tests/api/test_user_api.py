import pytest
from core.assertions import assert_key_in_response

@pytest.mark.api
class TestUserAPI:

    @pytest.mark.parametrize("page", [1, 2, 3])
    def test_get_users(self, user_api,page):
        response = user_api.get_users(page=page)
        assert response.status_code == 200

        body = response.json()
        assert "users" in body
        assert len(body["users"]) > 0

    def test_create_user(self, user_api):
        response = user_api.create_user("Sidharth", "QA Architect")
        assert response.status_code == 201

        body = response.json()
        assert body["firstName"] == "Sidharth"
