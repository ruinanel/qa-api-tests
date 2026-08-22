"""API-клиент — тонкая обёртка над requests.

Зачем обёртка, а не вызывать requests напрямую в каждом тесте:
  - базовый URL хранится в одном месте (тесты пишут только путь "/users/1");
  - единый таймаут на все запросы;
  - одна requests.Session (переиспользует соединение — быстрее);
  - логирование каждого запроса (видно, что реально ушло на сервер);
  - если завтра добавится авторизация/заголовки — правим тут, а не в 100 тестах.
"""

import logging

import requests

from config import BASE_URL, TIMEOUT

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        """Склеить базовый адрес и путь: _url('/users/1') -> 'https://.../users/1'."""
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, params: dict | None = None) -> requests.Response:
        """GET-запрос. params — словарь query-параметров, напр. {'userId': 1}."""
        url = self._url(path)
        logger.info("GET %s params=%s", url, params)
        response = self.session.get(url, params=params, timeout=self.timeout)
        logger.info("GET %s -> %s", url, response.status_code)
        return response

    def post(self, path: str, json: dict | None = None) -> requests.Response:
        """POST-запрос с телом в формате JSON."""
        url = self._url(path)
        logger.info("POST %s json=%s", url, json)
        response = self.session.post(url, json=json, timeout=self.timeout)
        logger.info("POST %s -> %s", url, response.status_code)
        return response
