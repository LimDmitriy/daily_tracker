# 📈 Daily Tracker
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)]()
[![Django](https://img.shields.io/badge/Django-5.x-success)]()
[![Django REST](https://img.shields.io/badge/DRF-3.x-red)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)]()
[![Redis](https://img.shields.io/badge/Redis-Broker-red)]()
[![Celery](https://img.shields.io/badge/Celery-Async%20Tasks-brightgreen)]()
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)]()
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-informational)]()
[![Tests](https://img.shields.io/badge/Tests-Pytest-yellow)]()
[![Coverage](https://img.shields.io/badge/Coverage-Enabled-brightgreen)]()
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black)]()
[![Lint](https://img.shields.io/badge/Lint-Flake8-orange)]()

---

## 📌 Описание проекта

**Daily Tracker** — это backend-приложение для отслеживания ежедневных задач и привычек, построенное на **Django + Django REST Framework**, с фоновой обработкой задач через **Celery + Redis** и хранением данных в **PostgreSQL**.  

Проект демонстрирует практические навыки:

- разработки REST API
- проектирования архитектуры backend-приложения
- работы с асинхронными задачами
- настройки Docker-инфраструктуры
- интеграции CI/CD
- написания тестов и обеспечения качества кода

---

## 🚀 Возможности проекта

### 📋 Управление задачами и привычками
Поддержка добавления, обновления и удаления задач и ежедневных записей.  
Реализована полноценная CRUD-логика через REST API.

---

### 🔁 REST API
API разработан с использованием **Django REST Framework** и готов для интеграции:
- с frontend-приложениями
- мобильными клиентами
- сторонними сервисами

---

### 🕒 Фоновые задачи
Используется **Celery + Redis** для выполнения:
- периодических задач (например, напоминания)
- длительных процессов (обработка данных, уведомления)

---

### 🗃 Хранение данных
В качестве основной базы данных используется **PostgreSQL**, обеспечивающая:
- надёжность хранения
- поддержку сложных запросов
- масштабируемость

---

### 🔐 Аутентификация JWT
Реализована авторизация через **JWT (SimpleJWT)**:
- безопасный доступ к API
- токены доступа и обновления
- разграничение прав пользователей

---

### 📡 Интеграция Telegram Bot
Поддержка взаимодействия через Telegram:
- отправка уведомлений
- возможная интеграция с задачами и привычками

---

### 🪪 Конфигурация через `.env`
Использование переменных окружения через **python-dotenv**:
- безопасное хранение секретов
- удобство деплоя
- разделение dev/prod конфигураций

---

### ⚙️ Документация API (Swagger)
Автоматическая генерация документации через **drf-spectacular**:
- OpenAPI-спецификация
- Swagger UI
- удобное тестирование эндпоинтов

---

### 🧪 Тестирование
Используется стек тестирования:
- **pytest**
- **pytest-django**
- **pytest-cov**

Реализовано покрытие кода и автоматический запуск тестов в CI.

---

### 🧹 Качество кода
Настроены инструменты поддержания качества:
- **Black** — автоформатирование
- **Flake8** — линтинг
- **Isort** — сортировка импортов

---

## 🚀 Установка и запуск

1. Клонирование репозитория
```
git clone https://github.com/LimDmitriy/daily_tracker
```
2. Установите зависимости:
```
poetry install
```
4. Применение миграций
```
python3 manage.py migrate
```
5. Запуск сервера
```
python3 manage.py runserver
```
--- 
## 📌 Используемый стек 

- Django 5+
- Django REST Framework
- JWT-аутентификация (SimpleJWT)
- PostgreSQL
- Celery + Redis
- Периодические задачи (django-celery-beat)
- Интеграция с Telegram Bot
- Swagger / OpenAPI (drf-spectacular)
- Docker и Docker Compose
- CI/CD pipeline
- Pytest + Coverage
- Инструменты качества кода (Black, Flake8, Isort)
- Настройка CORS

---

## 👨‍💻 Что я реализовал в этом проекте

- Спроектировал REST API с JWT-аутентификацией
- Реализовал асинхронную обработку задач через Celery
- Настроил Docker-инфраструктуру (web + db + redis + worker)
- Подключил CI/CD через GitHub Actions
- Реализовал тестирование с покрытием кода
- Настроил линтинг и автоформатирование
- Организовал переменные окружения через .env
- Подготовил Swagger-документацию

---