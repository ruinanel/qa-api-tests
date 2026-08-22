# API-автотесты (pytest + requests)

![API tests](https://github.com/ruinanel/qa-api-tests/actions/workflows/tests.yml/badge.svg)

Автотесты REST API на Python. Демонстрируют структуру фреймворка, API-клиент,
фикстуры, параметризацию, позитивные и негативные сценарии.

**Тестируемый API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — публичный REST API.

## Стек
- Python 3.12
- pytest — фреймворк тестирования
- requests — HTTP-клиент

## Структура
```
qa-api-tests/
├── api/
│   └── client.py        # ApiClient — обёртка над requests (base_url, timeout, session)
├── tests/
│   ├── conftest.py      # фикстура api (готовый клиент)
│   ├── test_users.py    # примеры тестов
│   └── test_your_turn.py
├── config.py            # BASE_URL, TIMEOUT
├── pytest.ini
└── requirements.txt
```

## Запуск
```bash
# создать окружение и поставить зависимости
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# запустить тесты
pytest -v
pytest -m smoke        # только дымовые
```

## Что покрыто
- GET: получение ресурса, проверка статус-кода и полей ответа
- Списки и query-параметры (фильтрация)
- POST: создание ресурса (201)
- Негативные сценарии (404)
- Параметризация
