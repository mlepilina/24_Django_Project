# 24_Django_Project

## Запуск приложения

```shell
python manage.py runserver
```


## Запуск Celery

```shell
celery -A config worker -l DEBUG -P eventlet
```


## Запуск Beat
```shell
celery -A config beat -l info
```
