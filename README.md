🚀 Inforce Lunch API

A clean and fully functional REST API that allows employees to select their lunch options for the day.  
This project was implemented as a technical assignment and follows clean and modular architecture principles.

---

## ⭐ Features

- User registration
- JWT-based authentication
- Restaurant creation and management
- Daily menu upload for restaurants (only **one menu per date** per restaurant)
- Employee accounts (`is_employee` flag)
- View today’s menu
- Submit employee lunch choice
- View aggregated results for today

---

## 🛠 Tech Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (JWT auth)
- PostgreSQL
- Docker & docker-compose
- pytest
- flake8

SQLite was used during local development, but the final setup runs on PostgreSQL in Docker.

---

## 📁 Project Structure

```text
project_root/
│── manage.py
│── Dockerfile
│── docker-compose.yml
│── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/
│   ├── models.py        # Custom User model with is_employee flag
│   ├── serializers.py   # UserSerializer, RegisterSerializer
│   ├── views.py         # Registration and user list
│   └── urls.py
│
├── restaurants/
│   ├── models.py        # Restaurant model
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── menus/
│   ├── models.py        # Menu and EmployeeChoice
│   ├── serializers.py
│   ├── permissions.py   # IsEmployee permission
│   ├── views.py
│   └── urls.py
│
├── requirements.txt
└── README.md
