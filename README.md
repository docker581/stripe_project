# stripe_project

## Описание проекта
Cервис для взаимодействия с платежной системой Stripe

## О платежной системе Stripe
https://stripe.com/docs

## Стек технологий
- Python 3.8
- Django 3.2
- Stripe 5.1.1
- Bootstrap 4.3.1

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/stripe_project
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск приложения
```bash
python manage.py runserver
```

### Пример файла .env
```bash
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
DOMAIN_URL=http://127.0.0.1:8000/
DEBUG=True
```
