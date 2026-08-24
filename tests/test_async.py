import asyncio

import allure


@allure.feature("Asyncio")
@allure.story("GET и asyncio.gather")
class TestGetsAsync:
    @allure.title("GET /users/1 через httpx")
    async def test_get_user_async(self, async_api):
        response = await async_api.get("/users/1")
        assert response.status_code == 200

    @allure.title("Работа с нескольким GET сразу. Gather")
    async def test_get_gather(self, async_api):
        responses = await asyncio.gather(*[async_api.get(f"/users/{i}") for i in range(1, 6)])
        for index, response in enumerate(responses):
            body = response.json()
            assert response.status_code == 200
            assert 'id' in body
            assert body["id"] == index + 1
