# -*- coding: utf-8 -*-
"""API-клиент — тонкая обёртка над requests.

Зачем обёртка, а не вызывать requests напрямую в каждом тесте:
  - базовый URL хранится в одном месте (тесты пишут только путь "/users/1");
  - единый таймаут на все запросы;
  - одна requests.Session (переиспользует соединение — быстрее);
  - если завтра добавится авторизация/заголовки — правим тут, а не в 100 тестах.

Помнишь День 3 (compose_url) и День 4 (класс с self)? Здесь это оживает.
"""
import requests

from config import BASE_URL, TIMEOUT


class ApiClient:
    def __init__(self, base_url=BASE_URL, timeout=TIMEOUT):
        self.base_url = base_url.rstrip("/")   # как в compose_url — убираем хвостовой слэш
        self.timeout = timeout
        self.session = requests.Session()

    def _url(self, path):
        """Склеить базовый адрес и путь: _url('/users/1') -> 'https://.../users/1'."""
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, params=None):
        """GET-запрос. params — словарь query-параметров, напр. {'userId': 1}."""
        return self.session.get(self._url(path), params=params, timeout=self.timeout)

    def post(self, path, json=None):
        """POST-запрос с телом в формате JSON."""
        return self.session.post(self._url(path), json=json, timeout=self.timeout)
