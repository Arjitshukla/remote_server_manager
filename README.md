# Remote Server Manager API

## Features
- User Authentication (JWT)
- Server CRUD (Add / List / Delete)
- SSH Command Execution
- Command Logging

## Setup
1. Clone repo
2. python -m venv venv
3. pip install -r requirements.txt
4. uvicorn app.main:app --reload

## Test
- Swagger UI: http://127.0.0.1:8000/docs

## to start docker for create shh server for demo
-docker-compose down
-docker-compose up --build -d
-docker ps

## Set environment variables
- Create a .env file in the root directory with:
```python
SECRET_KEY=<your secret key>
DATABASE_URL=<sqlite:///./app.db>
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
SENDGRID_API_KEY=<"you api key">

```

### Usage

- Register a new user via /auth/register
- Login via /auth/login to get JWT token
- Add a server via /servers/create
- Execute commands via /ssh/execute/{server_id}
- View command logs via /logs

## Images
![Medical Diagram](./app/static/Images/demo.png)