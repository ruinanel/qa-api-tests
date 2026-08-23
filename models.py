"""Pydantic-модели ответов API.

Зачем модели вдобавок к JSON Schema:
  - типобезопасность: user.email вместо resp.json()["email"] (автодополнение в IDE);
  - валидация «в одну строку»: User.model_validate(data) упадёт с понятной ошибкой,
    если структура или типы не совпали;
  - вложенные модели (User -> Address -> Geo) описывают контракт наглядно.
Лишние поля ответа pydantic по умолчанию игнорирует, поэтому модель может быть частичной.
"""

from pydantic import BaseModel


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    city: str
    zipcode: str
    geo: Geo


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str
