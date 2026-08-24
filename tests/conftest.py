"""Общие фикстуры для всех тестов."""

import pytest

from api.async_client import AsyncApiClient
from api.client import ApiClient


@pytest.fixture(scope="session")
def api():
    """Готовый API-клиент.
    scope="session" — создаётся ОДИН раз на весь прогон (не нужно поднимать
    клиента и сессию заново перед каждым тестом). Тесты только читают, состояние не портят.
    """
    return ApiClient()

@pytest.fixture(scope="session")
def async_api():
    """Готовый Async API-клиент.
    """
    return AsyncApiClient()
