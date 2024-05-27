FROM ubuntu:latest
LABEL authors="gimsanghae"
# Python 이미지를 기반으로 한 새 Docker 이미지를 생성합니다.
FROM python:3.11

# 작업 디렉토리를 설정합니다.
WORKDIR /app
# Poetry를 설치합니다.
RUN pip install poetry

# `pyproject.toml` 파일과 `poetry.lock` 파일을 Docker 이미지에 복사합니다.
COPY pyproject.toml poetry.lock ./

# 종속성을 설치합니다.
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# 애플리케이션 코드를 Docker 이미지에 추가합니다.
COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]