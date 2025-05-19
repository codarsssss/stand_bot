# Standing Bot 🤖

Telegram-бот, позволяющий отслеживать, у кого "стоит".

## 📁 Структура проекта

```
.
├── app/
│   ├── main.py           # точка входа
│   ├── config.py         # переменные окружения
│   ├── db.py             # работа с SQLite
│   ├── handlers.py       # логика Telegram
│   ├── keyboard.py       # inline-кнопки
│   ├── errors.py         # обработка ошибок
│   └── messages.py       # тексты для интернационализации
├── data/
│   ├── bot_data.db       # база данных
│   ├── .env              # переменные окружения
│   └── .env.example      # шаблон
├── tests/
│   └── test_db.py        # тесты
├── .flake8               # настройки линтера
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── Makefile
├── pyproject.toml        # poetry config
├── poetry.lock
└── .github/workflows/deploy.yml
```

## 🚀 Команды Make

### 📦 Docker

- `make build` — собрать контейнер
- `make up` — запустить контейнер
- `make down` — остановить
- `make restart` — перезапуск
- `make logs` — показать логи
- `make shell` — зайти внутрь
- `make ps` — статус

### 🛠 Разработка

- `make install` — Poetry-зависимости
- `make run` — локальный запуск
- `make lint` — flake8-проверка
- `make test` — pytest

### ⚙️ Окружение

- `make env` — показать `.env`
- `make env-example` — шаблон
- `make prepare-env` — скопировать шаблон

### 📡 Деплой

- `make deploy` — rsync + SSH на VPS  
  Требуется настроить `VPS_HOST`, `VPS_USER`, `VPS_PATH` в Makefile

### 💾 Бэкап

- `make backup` — сохранить `bot_data.db` в `backup/`

---

## ✅ CI/CD: Автоматический деплой

При коммите в `main`:

- ✅ Запускаются тесты (`make test`)
- ✅ Код деплоится на VPS через SSH
- ✅ Перезапускается контейнер

Файл: `.github/workflows/deploy.yml`

Secrets, которые надо задать в GitHub → Settings → Secrets:

```env
VPS_USER=user
VPS_HOST=1.2.3.4
VPS_PATH=/opt/stand_bot
VPS_SSH_KEY=<ssh-private-key>
```

---

## 🩺 Healthcheck и отладка

Команды:

- `/health` — бот работает ✅
- `/debug` — Chat ID, Title, Username

Доступ: **только ADMIN_CHAT_ID**  
Управляется через `.env`:

```env
DEBUG=True
ADMIN_CHAT_ID=123456789
```

---

## 🧪 Тесты

`pytest` с моками:

- `tests/test_db.py` проверяет SQLite
- изолированное окружение через `monkeypatch`

---

## 🌍 Интернационализация

Все ключевые сообщения вынесены в `messages.py`:

```python
MESSAGES = {
  "ru": { "enter_name": "...", "standing": "..." },
  "en": { "enter_name": "...", "standing": "..." }
}
```

Язык задаётся в `.env`:

```env
LANG=ru
```

---

Проект использует:

- Python 3.10+
- Poetry
- Docker + Compose
- GitHub Actions
- flake8 + pytest
- Telegram Bot API
- SQLite