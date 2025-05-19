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
│   └── errors.py         # обработка ошибок
├── data/
│   ├── bot_data.db       # база данных
│   ├── .env              # переменные окружения
│   └── .env.example      # шаблон
├── tests/
│   └── test_db.py        # тест на SQLite
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

### 📦 Работа с Docker

- `make build` — собрать контейнер
- `make up` — запустить контейнер в фоне
- `make down` — остановить контейнер
- `make restart` — перезапустить контейнер
- `make logs` — вывести логи
- `make shell` — зайти внутрь контейнера
- `make ps` — статус контейнеров

### 💻 Локальная разработка

- `make install` — установить зависимости через Poetry
- `make run` — запустить бота локально
- `make lint` — проверить стиль кода через flake8
- `make test` — запустить pytest с тестами

### ⚙️ Работа с окружением

- `make env` — показать текущий `.env`
- `make env-example` — показать `.env.example`
- `make prepare-env` — создать `.env`, если отсутствует

### 📡 Деплой на сервер

- `make deploy` — загрузить код на VPS и перезапустить бот  
  > Задай `VPS_HOST`, `VPS_USER`, `VPS_PATH` в `Makefile`

### 💾 Резервное копирование базы

- `make backup` — сохранить копию `bot_data.db` в папку `backup/`

### 🔧 CI/CD

- `make ci-build` — собрать Docker-образ для CI/CD без запуска

## 🩺 Healthcheck

Бот поддерживает команду `/health`  
Ответ: `✅ Бот работает.` — для проверки доступности из CI, мониторинга, и т.д.

## 🛠 Отладка

При установке `DEBUG=True` в `.env`, включается команда `/debug`, которая отвечает:
- Chat ID
- Название чата
- Username

> Используется для получения ID группы, проверки прав и тестов

## ✅ Тесты

Поддерживается `pytest`:
- тестируется работа с базой (`tests/test_db.py`)
- изолированное окружение через `monkeypatch`

## 🔐 Пример .env файла

```env
BOT_TOKEN=your_telegram_bot_token
GROUP_CHAT_ID=-1001234567890
DB_PATH=data/bot_data.db
ADMIN_CHAT_ID=123456789
DEBUG=True
```

---

Проект использует:

- Python 3.10
- Poetry для управления зависимостями
- Docker + Compose
- GitHub Actions (CI/CD)
- SQLite для хранения пользователей
- flake8 + pytest для проверки качества кода

## 🔒 Доступ только администраторам

Команды `/debug` и `/health` доступны только если `update.effective_user.id == ADMIN_CHAT_ID`  
Это защищает от утечек внутренней информации в продакшене.

---

## ✅ CI: запуск тестов автоматически

GitHub Actions запускает `pytest` при каждом коммите в `main`:

```yaml
- name: Run tests
  run: make test
```

Добавлено в `.github/workflows/deploy.yml`

---

## 🌍 Интернационализация

Структура сообщений может быть адаптирована под разные языки:

📁 `app/messages.py`
```python
MESSAGES = {
    "ru": {
        "enter_name": "Введите имя и фамилию в родительном падеже...",
        "standing": "У {name} сейчас стоит.",
        "not_standing": "У {name} перестал стоять.",
    },
    "en": {
        "enter_name": "Enter your name and surname...",
        "standing": "{name} is currently standing.",
        "not_standing": "{name} stopped standing.",
    },
}
```

Выбор языка — через `.env` переменную `LANG=ru` и:

```python
from app.config import LANG
from app.messages import MESSAGES

text = MESSAGES[LANG]["enter_name"]
```



## 🔐 Ограничение прав

Команды `/debug` и `/health` доступны только пользователю с `ADMIN_CHAT_ID`.

## 🌍 Интернационализация

Все ключевые сообщения вынесены в файл `messages.py`.  
Язык задаётся через `.env` переменную:

```env
LANG=ru  # или en
```

Пример структуры `MESSAGES`:

```python
MESSAGES = {
    "ru": {
        "enter_name": "Введите имя...",
        "standing": "У {name} сейчас стоит.",
    },
    "en": {
        "enter_name": "Enter your name...",
        "standing": "{name} is currently standing.",
    },
}
```

Это позволяет в будущем удобно добавлять новые языки.
