# proninteam_test


### Задача
Реализовать веб-сервис на базе Django, предоставляющий CRUD REST API
для групповых денежных сборов.

---

#### Запуск проекта

Создать .env файл.Пример:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='django-insecure-a8y71e7o7yeoe@hyp3db&%u-sz!+h72waq+2&=u@g-0=09q9lp'
```

В директории с проектом выполнить команду

```
docker compose up
```

Подключиться к контейнеру 

```
docker exec -it backend-backend-1 bash
```

В контейнере выполнить миграции

```
python manage.py migrate
```

Создать суперпользователя

```
python manage.py createsuperuser
```

Проект будет доступен по адресу http://localhost:8000/


#### Для заполнения БД тестовыми данными восполльзутесь следующей командой:
```
python manage.py filldatabase
```


#### Доступные эндпоинты

- admin/
- api/v1/collects/
- api/v1/collects/{id}
- api/v1/payments/

Аутентификация реализована с помощью djoser со всеми доступными эндпоиндами.
