import allure


@allure.feature("Posts")
@allure.story("Читаем посты")
class TestPosts:
    @allure.title("GET /posts/1 возвращает пост с нужными полями")
    def test_get_single_post(self, api):
        response = api.get("/posts/1")
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == 1
        assert "title" in body
        assert "body" in body

    @allure.title("Ответ приходит в формате JSON (Content-Type)")
    def test_content_type_is_json(self, api):
        response = api.get("/posts/1")
        assert "application/json" in response.headers["Content-Type"]

    @allure.title("GET /comments фильтруется по postId")
    def test_comments_filtered_by_post(self, api):
        with allure.step("Запросить комментарии поста 1"):
            response = api.get("/comments", params={"postId": 1})

        assert response.status_code == 200
        comments = response.json()
        assert len(comments) > 0
        assert all(c["postId"] == 1 for c in comments)
