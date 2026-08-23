import pytest


def test_get_nonexistent_user_returns_404(api):
    resp = api.get("/users/999")
    assert resp.status_code == 404


def test_filter_posts_by_user(api):
    resp = api.get("/posts", params={"userId": 1})
    assert resp.status_code == 200
    posts = resp.json()
    assert len(posts) > 0
    for item in posts:
        assert item["userId"] == 1


def test_create_post_returns_201(api):
    resp = api.post("/posts", json={"title": "qa", "body": "test", "userId": 1})
    assert resp.status_code == 201
    assert resp.json().get("title") == "qa"


@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (10, 200),
        (5, 200),
        (12, 404),
        (0, 404),
        (15, 404),
    ],
)
def test_users_status_codes(api, user_id, expected_status):
    resp = api.get(f"/users/{user_id}")
    assert resp.status_code == expected_status
