# -*- coding: utf-8 -*-
"""JSON-схемы ответов API.

Схема описывает СТРУКТУРУ ответа: какие поля обязательны и какого они типа.
Это мощнее, чем проверять поля по одному: одним махом валидируем весь контракт API.
Формат — JSON Schema (стандарт, международный).
"""

# Схема одного пользователя (GET /users/{id})
USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
}

# Схема одного поста (GET /posts/{id})
POST_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id": {"type": "integer"},
        "userId": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}
