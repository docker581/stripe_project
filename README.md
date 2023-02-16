# stripe_project

## Описание проекта
Cервис для взаимодействия с платежной системой Stripe

### О платежной системе Stripe
https://stripe.com/docs

## Стек технологий
- Python 3.8
- Django 3.2
- Stripe 5.1.1
- Bootstrap 4.3.1
- Docker-compose 3.8
- Postgres 12.4
- Nginx 1.19.3
- Gunicorn 20.0.4

## Установка docker
https://docs.docker.com/engine/install/

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/stripe_project
```

### Пример файла .env
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
DOMAIN_URL=http://127.0.0.1/
DEBUG=True
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres
DB_HOST=db 
DB_PORT=5432

В случае, когда используется не локальный сервер, помимо переменной окружения DOMAIN_URL
нужно также изменить строку в nginx/default.conf:
```bash
server_name [your_ip];
```

### Запуск приложения
```bash
docker-compose up -d
```

### Выполнение миграций, создание суперпользователя и подключение статики
```bash
docker-compose exec web python manage.py migrate --noinput
```
```bash
docker-compose exec web python manage.py createsuperuser
```
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

## Функционал
GET /buy/{id} - получение Stripe Session Id для оплаты выбранного Order
GET /order/{id} - получение HTML-страницы с выбранным Order и кнопкой Buy, в дальнейшем - редирект на Stripe Checkout
Заказы (Order) и Единицы товаров (Item) создаются в админке.

## Автор
Докторов Денис
