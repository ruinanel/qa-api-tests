from api.validation import assert_valid_schema
from schemas import POST_SCHEMA, USER_SCHEMA


def test_user_matches_schema(api):
    resp = api.get("/users/1")
    assert resp.status_code == 200
    assert_valid_schema(resp.json(), USER_SCHEMA)  # проверяем всю структуру разом


def test_post_matches_schema(api):
    resp = api.get("/posts/1")
    assert resp.status_code == 200
    assert_valid_schema(resp.json(), POST_SCHEMA)
