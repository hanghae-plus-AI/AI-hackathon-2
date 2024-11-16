FROM python:3.10

WORKDIR /app

RUN pip install poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --only main

COPY /app/ /app

CMD ["poetry", "run", "python", "main.py"]