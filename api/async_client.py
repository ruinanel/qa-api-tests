import logging

import httpx

from config import BASE_URL, TIMEOUT

logger = logging.getLogger(__name__)


class AsyncApiClient:
    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    async def get(self, path: str, params: dict | None = None) -> httpx.Response:
        logger.info("GET url=%s", path)
        async with httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout) as client:
            return await client.get(path, params=params)

    async def post(self, path: str, json: dict | None = None) -> httpx.Response:
        logger.info("POST %s json=%s", path, json)
        async with httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout) as client:
            return await client.post(path, json=json)
