# 🛒 OpenCart — QA проект с Page Object Model

Четвёртый учебный проект по QA-автоматизации.
Браузерные тесты для реального сайта ecommerce-playground.lambdatest.io
через Playwright с паттерном Page Object Model.

## Что я делал

Самостоятельно выбрал реальный демо-сайт интернет-магазина и написал
браузерные тесты через Playwright. В отличие от предыдущих проектов —
никаких готовых локаторов, всё искал сам через DevTools браузера
и Playwright Codegen. Написал 19 тестов покрывающих основные
пользовательские сценарии.

## Чему научился

- Применил паттерн Page Object Model на реальном сайте
- Научился самостоятельно находить локаторы через DevTools
- Использовал get_by_role вместо хрупких CSS-селекторов
- Выносил локаторы в константы класса для удобной поддержки
- Добавил типизацию методов (-> bool, -> str)
- Разобрался с wait_for_selector и wait_for_load_state
- Научился использовать Playwright Codegen для записи действий
- Написал Dockerfile для запуска тестов в изолированном контейнере

## Что тестировал

| Раздел | Тестов |
|--------|--------|
| Главная страница | 4 |
| Поиск | 3 |
| Каталог | 3 |
| Страница товара | 4 |
| Корзина | 4 |
| Авторизация | 2 |
| Итого | 19 |

## Структура проекта

```
opencart_pom/
├── pages/
│   ├── base_page.py          ← общие методы для всех страниц
│   ├── search_page.py        ← поиск
│   ├── catalog_page.py       ← каталог и категории
│   ├── product_page.py       ← страница товара
│   ├── cart_page.py          ← корзина
│   └── authorization_page.py ← авторизация
├── tests/
│   └── test_shop.py          ← все тесты
├── conftest.py               ← fixtures
├── Dockerfile                ← запуск тестов в контейнере
├── requirements.txt
└── README.md
```

## Запуск локально

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v --html=report.html --self-contained-html
```

## Запуск через Docker

```bash
docker build -t opencart-tests .
docker run opencart-tests
```

## Стек

- Python 3.12
- Playwright + pytest-playwright
- pytest + pytest-html
- Page Object Model
- Docker