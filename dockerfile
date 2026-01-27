FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]