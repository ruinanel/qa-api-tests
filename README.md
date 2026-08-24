# API-автотесты на Python

![API tests](https://github.com/ruinanel/qa-api-tests/actions/workflows/tests.yml/badge.svg)
![Allure report](https://github.com/ruinanel/qa-api-tests/actions/workflows/allure.yml/badge.svg)

📊 **Live Allure-отчёт:** https://ruinanel.github.io/qa-api-tests/ (обновляется в CI)

Фреймворк автотестов REST API на Python. Демонстрирует слоистую архитектуру,
синхронный и асинхронный API-клиенты, фикстуры, параметризацию, data-driven,
несколько стратегий валидации ответа (голые ассерты, JSON Schema, pydantic-модели),
позитивные и негативные сценарии, отчёты Allure и CI с линтингом и проверкой типов.

**Тестируемый API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — публичный REST API.
API тренировочный (POST не персистит данные), поэтому фреймворк переносится на реальный
сервис заменой `BASE_URL` и схем.

## Стек

Python 3.12

**Runtime** (`requirements.txt`):
- pytest — фреймворк тестирования
- requests — синхронный HTTP-клиент
- httpx — асинхронный HTTP-клиент
- pydantic — типобезопасная валидация ответов через модели
- jsonschema — валидация ответов по JSON Schema
- allure-pytest — отчёты Allure
- pytest-xdist — параллельный прогон тестов
- pytest-asyncio — поддержка async-тестов

**Dev** (`requirements-dev.txt`):
- ruff — линтер и форматтер
- mypy — статическая проверка типов
- pre-commit — хуки перед коммитом

## Структура

```
qa-api-tests/
├── api/
│   ├── client.py              # ApiClient — обёртка над requests (session, retry, timeout, логи)
│   ├── async_client.py        # AsyncApiClient — асинхронный клиент на httpx
│   └── validation.py          # проверка ответа по JSON Schema
├── tests/
│   ├── conftest.py            # фикстуры api / async_api
│   ├── test_users.py          # GET, проверка полей, список, smoke-маркер
│   ├── test_posts.py          # посты, Content-Type, фильтрация комментариев
│   ├── test_check_status_code.py  # 404, POST 201, параметризованная матрица статусов
│   ├── test_schema.py         # валидация ответа по JSON Schema
│   ├── test_models.py         # валидация через pydantic-модели
│   ├── test_data_driven.py    # тест-данные из data/users.json
│   └── test_async.py          # асинхронные запросы (asyncio.gather)
├── data/
│   └── users.json             # тест-данные для data-driven
├── models.py                  # pydantic-модели ответов (User, Post, Address, Geo)
├── schemas.py                 # JSON-схемы ответов
├── config.py                  # BASE_URL, TIMEOUT (переопределяются через env)
├── pytest.ini
├── pyproject.toml             # настройки ruff и mypy
├── requirements.txt
├── requirements-dev.txt
├── .pre-commit-config.yaml
└── .github/workflows/         # CI: тесты + публикация Allure-отчёта
```

## Запуск

```bash
# создать окружение и поставить зависимости
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# для линтера/типов/хуков (по желанию)
pip install -r requirements-dev.txt

# запустить тесты
pytest -v
pytest -m smoke        # только дымовые
pytest -n auto         # параллельный прогон
```

## Что покрыто

- **GET**: получение ресурса, проверка статус-кода и полей ответа
- **Списки и query-параметры**: фильтрация (`?userId=`, `?postId=`)
- **POST**: создание ресурса (201)
- **Негативные сценарии**: 404 на несуществующий ресурс
- **Параметризация**: матрица «id → ожидаемый статус»
- **Data-driven**: тест-кейсы из отдельного JSON-файла
- **Валидация по JSON Schema**: сверка всей структуры ответа со схемой
- **Валидация через pydantic-модели**: типобезопасный разбор, в т.ч. вложенные модели (User → Address → Geo)
- **Асинхронные запросы**: несколько GET одновременно через `asyncio.gather` (httpx)
- **Content-Type**: проверка формата ответа

## Особенности фреймворка

- **API-клиент с ретраями**: автоповтор на `429/5xx` с экспоненциальным backoff (`api/client.py`)
- **Конфигурация через env**: `BASE_URL` и `TIMEOUT` переопределяются переменными окружения (`config.py`)
- **Логирование** запросов и статусов ответов

## Allure-отчёт

Тесты умеют отдавать результаты в Allure.

```bash
# 1) прогнать тесты с сохранением результатов
pytest --alluredir=allure-results

# 2) посмотреть отчёт (нужна Java; allure запускаем через npx — ставить глобально не нужно)
npx allure-commandline serve allure-results
```

Живой отчёт публикуется автоматически: https://ruinanel.github.io/qa-api-tests/

## CI/CD

Настроено в `.github/workflows/`:

- **Линтинг и типы** отдельным job'ом: `ruff check`, `ruff format --check`, `mypy`
- **Матрица версий**: прогон тестов на Python 3.11 и 3.12
- **Параллельный прогон**: `pytest -n auto`
- **Ночной запуск** по расписанию (cron, 03:00 UTC)
- **Автопубликация Allure-отчёта** на GitHub Pages (с сохранением истории для трендов)

Локально те же проверки перед коммитом выполняет **pre-commit** (`ruff` + `ruff-format`):

```bash
pre-commit install
```

## Качество кода

- **ruff** — линтер и форматтер (правила E, W, F, I, UP, B; настройки в `pyproject.toml`)
- **mypy** — статическая проверка типов
- Аннотации типов в клиентах и фикстурах
