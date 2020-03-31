FROM python:3.7 AS base

WORKDIR /usr/src/app

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-dev


FROM base AS app

COPY ./django_test ./django_test


FROM base AS base-dev

RUN poetry install


FROM base-dev as dev

COPY . .
