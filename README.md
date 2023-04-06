## Парсер цен АЗС

Привет! Это тестовое задание для ООО О2

Приложение парсит данные с сайта https://rss.tatneft.ru/prod
раз в 30 дней, и затем обновляет данные в БД

Стек:
Django 4.2,
DRF,
Postgresql

## Docker

С помощью Docker вы сможете легко установить это приложение

```sh
docker-compose -f docker-compose.yml up
```

После того как вы запустили Docker, подождите создание образа.
Программа запустится, далее будет отсчёт 43200 минут (30 дней).
Но в рамках проверки задания, чтобы вы не ждали 30 дней, 
я по заботился о вас и поставил таймер в 1 минуту.
По прошествии 1 минуты вы увидите в консоле имитацию кликов пользователя по сайту,
далее скачивается нужный файл, и с него записываются данные в БД.

После того как БД обновились вы сможете проверить данные через API
по ссылке http://127.0.0.1:8000/api/get_dt/


