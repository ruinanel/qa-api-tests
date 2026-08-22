"""ТВОИ ЗАДАНИЯ — напиши API-тесты. Образец — в tests/test_users.py.
Замени каждый pytest.fail(...) на настоящие проверки, добейся зелёного.

Запуск:  pytest tests/test_your_turn.py -v

Полезное:
  response = api.get("/путь")              # GET
  response = api.get("/posts", params={"userId": 1})   # GET с query-параметрами
  response = api.post("/posts", json={...})            # POST с телом
  response.status_code                      # число, напр. 200
  response.json()                           # тело ответа (dict или list)
"""

import pytest


def test_get_nonexistent_user_returns_404(api):
    """GET несуществующего пользователя /users/999 должен вернуть статус 404.
    (Негативный тест — проверяем поведение на «плохих» данных.)
    """
    resp = api.get("/users/999")
    assert resp.status_code == 404


def test_filter_posts_by_user(api):
    """GET /posts с параметром userId=1 (api.get('/posts', params={'userId': 1})).
    Проверь: статус 200 И у КАЖДОГО поста в ответе поле 'userId' равно 1.
    Подсказка: all(post['userId'] == 1 for post in response.json())
    """
    resp = api.get("/posts", params={"userId": 1})
    assert resp.status_code == 200
    posts = resp.json()
    assert len(posts) > 0
    for item in posts:
        assert item["userId"] == 1


def test_create_post_returns_201(api):
    """POST /posts с телом {'title': 'qa', 'body': 'test', 'userId': 1}.
    Проверь: статус 201 И что в ответе поле 'title' == 'qa'.
    """
    resp = api.post("/posts", json={"title": "qa", "body": "test", "userId": 1})
    assert resp.status_code == 201
    assert resp.json().get("title") == "qa"


@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        # TODO: заполни 3+ набора (id пользователя, ожидаемый статус)
        # существующие: 1..10 -> 200; несуществующие -> 404
        # например: (1, 200),
        (1, 200),
        (10, 200),
        (5, 200),
        (12, 404),
        (0, 404),
        (15, 404),
    ],
)
def test_users_status_codes(api, user_id, expected_status):
    """Параметризованный тест: GET /users/{user_id} должен вернуть expected_status.
    Заполни список наборов выше (минимум 3: и валидные, и невалидный).
    """
    resp = api.get(f"/users/{user_id}")
    assert resp.status_code == expected_status
