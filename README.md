# proninteam_test


### Задача
Реализовать веб-сервис на базе Django, предоставляющий CRUD REST API
для групповых денежных сборов.

---

#### Запуск проекта

Создать .env файл.

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
Собрать статику
```
python manage.py collectstatic
```
Проект будет доступен по адресу http://localhost/


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
