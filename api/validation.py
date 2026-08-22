# -*- coding: utf-8 -*-
"""Помощник для проверки ответа по JSON-схеме."""
from jsonschema import validate


def assert_valid_schema(data, schema):
    """Проверить, что data соответствует schema.
    Если структура/типы не совпадают — jsonschema бросит ValidationError,
    и тест упадёт с понятным сообщением (какое поле и что не так).
    """
    validate(instance=data, schema=schema)
