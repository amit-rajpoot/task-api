# ✅ Task API

> 🚀 A RESTful **Task Management API** built with **FastAPI**, featuring user authentication, JWT-based authorization, task CRUD operations, and database integration.

Task API is a backend project designed to manage users and their tasks through a clean and structured REST API.

---

## ✨ Features

* 👤 User registration
* 🔐 JWT authentication
* 🎟️ Access token generation
* 🔒 Protected API endpoints
* ✅ Create tasks
* 📋 Get user tasks
* 🔍 Get task by ID
* ✏️ Update tasks
* 🗑️ Delete tasks
* 👥 User-specific task ownership
* 🗄️ SQLAlchemy database integration
* ✔️ Request & response validation with Pydantic
* 📚 Automatic Swagger API documentation
* ⚡ Fast and lightweight REST API

---

## 🧠 How It Works

```text
                    👤 User
                      │
                      ▼
               ┌──────────────┐
               │   Register   │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │     Login    │
               └──────┬───────┘
                      │
                      ▼
                 🔑 JWT Token
                      │
                      ▼
               ┌──────────────┐
               │ Authenticated│
               │   Requests   │
               └──────┬───────┘
                      │
                      ▼
              ┌────────────────┐
              │  Task CRUD API  │
              └───────┬────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Create       Update      Delete
          │           │           │
          └───────────┼───────────┘
                      ▼
                  🗄️ Database
```

---

## 🔐 Authentication Flow

The API uses **JWT (JSON Web Token)** authentication to protect task endpoints.

```text
1️⃣ Register User
       ↓
2️⃣ Login
       ↓
3️⃣ Receive JWT Access Token
       ↓
4️⃣ Send Token with Request
       ↓
5️⃣ Token Verification
       ↓
6️⃣ Access Protected Task Routes
```

Example authorization header:

```text
Authorization: Bearer <access_token>
```

---

## 🔗 API Endpoints

### 👤 Authentication

| Method | Endpoint         | Description                |
| :----: | ---------------- | -------------------------- |
| `POST` | `/auth/register` | Register a new user        |
| `POST` | `/auth/token`    | Login and get access token |

### ✅ Tasks

|  Method  | Endpoint      | Description         |
| :------: | ------------- | ------------------- |
|  `POST`  | `/tasks`      | Create a new task   |
|   `GET`  | `/tasks`      | Get user's tasks    |
|   `GET`  | `/tasks/{id}` | Get a specific task |
|   `PUT`  | `/tasks/{id}` | Update a task       |
| `DELETE` | `/tasks/{id}` | Delete a task       |

> 🔒 Task endpoints require authentication.

---

## 🛠️ Tech Stack

| Technology                        | Purpose                    |
| --------------------------------- | -------------------------- |
| 🐍 **Python**                     | Programming language       |
| ⚡ **FastAPI**                     | REST API framework         |
| 🗄️ **SQLAlchemy**                | ORM / Database interaction |
| 🔐 **JWT**                        | Authentication             |
| 🔑 **Passlib / Password Hashing** | Password security          |
| 📦 **Pydantic**                   | Data validation            |
| 🚀 **Uvicorn**                    | ASGI server                |
| 🐘 **PostgreSQL / SQLite**        | Database                   |

---


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-api.git
```

### 2. Enter the project

```bash
cd task-api
```

### 3. Create virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate virtual environment

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ Never commit your `.env` file or secret keys to GitHub.

---

## ▶️ Run the API

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to:

* Register users
* Login
* Authorize using JWT
* Create tasks
* Update tasks
* Delete tasks
* Test protected endpoints

---

## 📝 Example Task

```json
{
  "title": "Learn FastAPI",
  "description": "Build a Task Management API",
  "priority": "HIGH",
  "due_date": "2026-09-20T18:00:00"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Build a Task Management API",
  "completed": false,
  "priority": "HIGH",
  "owner_id": 1
}
```

---

## 🗄️ Database Relationship

```text
┌──────────────┐
│     User     │
├──────────────┤
│ id           │
│ email        │
│ password     │
│ is_active    │
└──────┬───────┘
       │
       │ 1 : Many
       ▼
┌──────────────┐
│     Task     │
├──────────────┤
│ id           │
│ title        │
│ description  │
│ completed    │
│ priority     │
│ due_date     │
│ owner_id     │
└──────────────┘
```

Each task belongs to a specific user, so authenticated users can access and manage their own tasks.

---


## 🚧 Project Status

```text
🟢 Active Development
```

The project is being developed as part of my journey to build real-world backend applications with **Python and FastAPI**.

---

## 👨‍💻 Author

### Amit Rajpoot

Backend developer focused on building projects with:

**Python • FastAPI • SQLAlchemy • PostgreSQL • REST APIs**

---

## ⭐ Support

If you like this project:

```text
⭐ Star the repository
🍴 Fork the repository
🐛 Report issues
💡 Suggest improvements
```

---

### ❤️ Built with Python & FastAPI

```text
        🐍 Python
            │
            ▼
       ⚡ FastAPI
            │
       ┌────┴────┐
       ▼         ▼
    🔐 Auth    ✅ Tasks
       │         │
       └────┬────┘
            ▼
       🗄️ Database
```
