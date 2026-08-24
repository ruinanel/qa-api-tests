from models import Post, User


def test_user_matches_pydantic_model(api):
    resp = api.get("/users/1")
    user = User.model_validate(resp.json())  # упадёт, если структура/типы не совпали

    assert user.id == 1
    assert "@" in user.email
    assert user.address.city  # доступ к вложенной модели Address


def test_post_matches_pydantic_model(api):
    resp = api.get("/posts/1")
    post = Post.model_validate(resp.json())

    assert post.id == 1
    assert post.userId > 0
