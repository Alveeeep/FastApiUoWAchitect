## RESTful приложение на [FastApi](https://github.com/fastapi/fastapi) для администрирования онлайн выставки котят
### Тестовое задание

## Технологии:
### - [PostgreSQL](https://www.postgresql.org)
### - [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
### - [Alembic](https://github.com/sqlalchemy/alembic)

## Использование

Запустите создание [Docker](https://github.com/docker) контейнера:
```sh
docker compose build
```

Запустите Docker-compose:
```sh
docker compose up -d
```

### Перейдите по адресу http://localhost:7667/docs#/

### Минимальные данные для проверки приложения подгружаются с помощью *Alembic*

### Использовался поведенческий паттерн [Unit of work](https://habr.com/ru/articles/808817/)
