# 🌿 GreenTree Backend Project

A simple backend built with **Django** and **Django REST Framework** for managing and serving extraction records via RESTful APIs, documented through **Swagger UI**.

---

## 🚀 Features

- CRUD operations for extraction records (Create, Read, Update, Delete)
- REST API with JSON responses
- Swagger documentation for interactive API testing
- Modular Django structure for easy extension

---

## 🧩 Tech Stack

- **Python 3.13**
- **Django 5.2**
- **Django REST Framework**
- **drf-yasg** (for Swagger documentation)

---

## ⚙️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/quintinlf/greentree-backend-project.git
   cd greentree-backend-project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The app will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Swagger docs: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## 🧠 Example Usage

**POST new record**
```
POST /api/records/
{
  "name": "test extraction",
  "value": 3.14
}
```

**Response**
```
{
  "id": 1,
  "name": "test extraction",
  "value": 3.14,
  "created_at": "2025-10-26T01:14:28.767357Z"
}
```

---

## 🔐 Environment Variables

See `.env.example` for required environment setup.

---

## 🧭 Future Improvements

- Add data visualizations using Matplotlib or Plotly
- Integrate with Azure SQL or PostgreSQL
- Extend models to represent real-world data (chemical, financial,statistical, etc.)
- Add authentication for user-specific records

---

## 📚 Learning Outcomes

This project demonstrates:

- Backend architecture fundamentals — how to structure a Django project and connect apps together.
- Database modeling with Django ORM — creating models that store and organize meaningful data.
- REST API design — exposing endpoints for other code, apps, or clients to interact with your data.
- Professional documentation with Swagger — creating interactive, shareable API docs.
- Local development and dependency management — using virtual environments, pip, migrations, and the runserver.

This is the bridge between personal scripts and scalable backend systems — useful for anything from trading bots, NMR analyzers, to personal apps.

---

👨🏾‍💻 Author: Quintin  
📅 Date: October 2025