FROM python:3.13-rc-slim

WORKDIR /app

# Poetry
RUN pip install poetry

# Копируем зависимости
COPY pyproject.toml poetry.lock ./

# Копируем код как пакет
COPY app/ ./app/
COPY data/ ./data/
COPY README.md ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

# Запускаем как пакет
CMD ["python", "-m", "app.main"]
