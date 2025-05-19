# ==========
# НАСТРОЙКИ
# ==========
COMPOSE=docker compose
PROJECT_NAME=standing_bot
SERVICE_NAME=bot
VPS_USER=root                 # Пользователь на сервере
VPS_HOST=your.server.ip       # IP-адрес сервера
VPS_PATH=/opt/stand_bot       # Путь на сервере, куда загружается бот

# ======================
# ЛОКАЛЬНАЯ РАЗРАБОТКА
# ======================

# Установка зависимостей через Poetry
install:
	poetry install

# Запуск бота локально
run:
	poetry run python app/main.py

# Линтинг кода (если установлен flake8)
lint:
	poetry run flake8 app/

# ====================
# РАБОТА С DOCKER
# ====================

# Сборка контейнера
build:
	$(COMPOSE) build

# Запуск контейнера в фоне
up:
	$(COMPOSE) up -d

# Остановка контейнера
down:
	$(COMPOSE) down

# Перезапуск контейнера
restart: down up

# Просмотр логов
logs:
	$(COMPOSE) logs -f

# Тесты
test:
	PYTHONPATH=./ poetry run pytest tests


# =====================
# УТИЛИТЫ И ОТЛАДКА
# =====================

# Список контейнеров
ps:
	$(COMPOSE) ps

# Вход в контейнер
shell:
	$(COMPOSE) exec $(SERVICE_NAME) /bin/sh

# =====================
# РАБОТА С ОКРУЖЕНИЕМ
# =====================

# Показать текущий .env
env:
	@cat .env

# Показать .env.example
env-example:
	@cat .env.example

# Создание .env из .env.example, если не существует
prepare-env:
	@if [ ! -f .env ]; then \
		echo "Файл .env не найден, копируем из .env.example..."; \
		cp .env.example .env; \
	else \
		echo ".env уже существует"; \
	fi

# =====================
# ДЕПЛОЙ НА VPS
# =====================

# Загрузка кода на сервер и перезапуск через SSH
deploy:
	scp -r . $(VPS_USER)@$(VPS_HOST):$(VPS_PATH)
	ssh $(VPS_USER)@$(VPS_HOST) 'cd $(VPS_PATH) && docker compose down && docker compose up -d --build'

# =========================
# РЕЗЕРВНАЯ КОПИЯ БАЗЫ
# =========================

# Создание резервной копии базы SQLite
backup:
	mkdir -p backup
	cp data/bot_data.db backup/bot_data_$(shell date +%Y-%m-%d_%H-%M-%S).db

# =========================
# CI-СБОРКА (без запуска)
# =========================

# Сборка образа без запуска (для CI/CD)
ci-build:
	docker build -t $(PROJECT_NAME):ci .
