FROM  python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/"

COPY ./pyproject.toml /
COPY ./poetry.lock /

RUN apt-get update  -y && apt-get install curl -y \
&& curl -sSL https://install.python-poetry.org | python3 - \
&& poetry config virtualenvs.create false \
&& poetry install \
&& apt-get remove curl -y \
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* 

COPY ./app /
WORKDIR /app