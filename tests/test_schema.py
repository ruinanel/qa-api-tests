"""Валидация ответов по JSON-схеме.
Запуск:  pytest tests/test_schema.py -v
"""


from api.validation import assert_valid_schema
from schemas import POST_SCHEMA, USER_SCHEMA


# --- ПРИМЕР (проходит) ---
def test_user_matches_schema(api):
    resp = api.get("/users/1")
    assert resp.status_code == 200
    assert_valid_schema(resp.json(), USER_SCHEMA)  # проверяем всю структуру разом


# --- ТВОЁ ЗАДАНИЕ ---
def test_post_matches_schema(api):
    """Запроси GET /posts/1, проверь статус 200 и валидность по POST_SCHEMA.
    Ориентир — тест выше. POST_SCHEMA уже готова в schemas.py.
    """
    resp = api.get("/posts/1")
    assert resp.status_code == 200
    assert_valid_schema(resp.json(), POST_SCHEMA)
