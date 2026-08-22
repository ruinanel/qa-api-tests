"""Помощник для проверки ответа по JSON-схеме."""

from typing import Any

from jsonschema import validate


def assert_valid_schema(data: Any, schema: dict) -> None:
    """Проверить, что data соответствует schema.
    Если структура/типы не совпадают — jsonschema бросит ValidationError,
    и тест упадёт с понятным сообщением (какое поле и что не так).
    """
    validate(instance=data, schema=schema)
