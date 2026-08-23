import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import BASE_URL, TIMEOUT

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT, retries: int = 3) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

        # Ретраи с экспоненциальным backoff на временные сбои сети/сервера.
        retry = Retry(
            total=retries,
            backoff_factor=0.5,  # паузы ~0.5s, 1s, 2s между попытками
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

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
