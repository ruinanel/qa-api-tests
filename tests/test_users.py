# -*- coding: utf-8 -*-
"""ПРИМЕРЫ рабочих API-тестов. Читай, запускай, бери за образец.
Запуск:  pytest tests/test_users.py -v
"""


def test_get_user_returns_200(api):
    # Arrange + Act
    response = api.get("/users/1")
    # Assert
    assert response.status_code == 200


def test_get_user_has_expected_fields(api):
    response = api.get("/users/1")
    body = response.json()          # тело ответа как словарь Python

    assert body["id"] == 1
    assert "email" in body          # поле email присутствует
    assert "@" in body["email"]     # и похоже на email


import pytest


@pytest.mark.smoke
def test_users_list_returns_ten(api):
    response = api.get("/users")
    body = response.json()          # тут тело — это список словарей

    assert response.status_code == 200
    assert isinstance(body, list)
    assert len(body) == 10
