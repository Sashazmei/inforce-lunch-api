# Inforce Lunch API

REST API для выбора обеда сотрудниками компании.  
Проект реализован как тестовое задание.

## Функциональность

- Регистрация пользователей
- Token-аутентификация
- Создание ресторанов
- Загрузка меню ресторана на каждый день (одно меню на дату)
- Создание сотрудников (флаг `is_employee`)
- Получение меню на текущий день
- Отправка выбора сотрудника по меню
- Получение результатов выборов на текущий день

## Стек

- Python 3.12
- Django
- Django REST framework
- DRF Token Authentication
- SQLite (по умолчанию, можно легко заменить на PostgreSQL)

## Структура проекта

```text
project_root/
│── manage.py
│── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/
│   ├── models.py        # кастомная модель User с полем is_employee
│   ├── serializers.py   # UserSerializer, RegisterSerializer
│   ├── views.py         # регистрация и список пользователей
│   └── urls.py
│
├── restaurants/
│   ├── models.py        # модель Restaurant
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── menus/
│   ├── models.py        # Menu и EmployeeChoice
│   ├── serializers.py
│   ├── permissions.py   # IsEmployee
│   ├── views.py
│   └── urls.py
│
└── README.md
