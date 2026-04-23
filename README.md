# Task Manager API
 
A production-style REST API built with FastAPI for managing tasks. Features JWT authentication, role-based access, and full task CRUD operations.
 
## Features
 
- JWT Authentication — access token + refresh token
- Password hashing with bcrypt
- Task CRUD — create, read, update, delete
- Task assignment — assign tasks to other users
- Protected routes — only authenticated users can access
- Role-based structure — admin and user roles
- Auto-generated Swagger documentation
## Tech Stack
 
- **FastAPI** — web framework
- **PostgreSQL** — database
- **SQLAlchemy** — ORM
- **Pydantic v2** — data validation
- **python-jose** — JWT tokens
- **passlib** — password hashing
- **Alembic** — database migrations
## Project Structure
 
```
app/
├── main.py
├── database.py
├── dependencies.py
├── core/
│   ├── config.py
│   └── security.py
├── models/
│   ├── user.py
│   └── task.py
├── schemas/
│   ├── user.py
│   └── task.py
├── services/
│   ├── auth_service.py
│   └── task_service.py
└── api/
    └── routes/
        ├── auth.py
        └── tasks.py
```
 
## Getting Started
 
### Prerequisites
 
- Python 3.10+
- PostgreSQL
### Installation
 
1. Clone the repository
```bash
git clone https://github.com/your-username/task-manager-api
cd task-manager-api
```
 
2. Install dependencies
```bash
pip install -r requirements.txt
```
 
3. Create `.env` file in root directory
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```
 
4. Run the server
```bash
uvicorn app.main:app --reload
```
 
5. Open Swagger docs
```
http://127.0.0.1:8000/docs
```
 
## API Endpoints
 
### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login and get tokens |
| GET | /auth/me | Get current user |
| POST | /auth/refresh | Refresh access token |
 
### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks/ | Create new task |
| GET | /tasks/ | Get all your tasks |
| GET | /tasks/{task_id} | Get task by ID |
| PUT | /tasks/{task_id} | Update task |
| DELETE | /tasks/{task_id} | Delete task |
 
## Environment Variables
 
| Variable | Description |
|----------|-------------|
| DATABASE_URL | PostgreSQL connection string |
| SECRET_KEY | JWT signing secret |
| ACCESS_TOKEN_EXPIRE_MINUTES | Access token expiry (default: 30) |
| REFRESH_TOKEN_EXPIRE_DAYS | Refresh token expiry (default: 7) |
