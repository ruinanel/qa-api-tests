import allure
import pytest


@allure.feature("Users")  # группировка в отчёте: раздел «Users»
class TestUsers:
    @allure.title("GET /users/1 возвращает статус 200")
    def test_get_user_returns_200(self, api):
        response = api.get("/users/1")
        assert response.status_code == 200

    @allure.title("Пользователь содержит ожидаемые поля")
    def test_get_user_has_expected_fields(self, api):
        response = api.get("/users/1")
        body = response.json()

        assert body["id"] == 1
        assert "email" in body
        assert "@" in body["email"]

    @allure.title("Список пользователей содержит 10 записей")
    @pytest.mark.smoke
    def test_users_list_returns_ten(self, api):
        with allure.step("Запросить список пользователей"):
            response = api.get("/users")

        assert response.status_code == 200
        body = response.json()
        assert isinstance(body, list)
        assert len(body) == 10
