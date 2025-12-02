# TaskFlow API
TaskFlow API is the backend of a simple task management system.  
It provides user authentication and task CRUD operations through a RESTful API.  
Built with Django REST Framework and JWT authentication, designed as part of a study/learning project.

## Features
- [JWT authentication](https://jwt.io/)
- User registration & login
- Tasks owned by individual users
- CRUD operations for tasks
- User-level permissions (each user sees only their own tasks)

## Tech stack
- Python 3.x
- Django
- Django REST Framework
- SimpleJWT
- PostgreSQL

## Project structure
```commandline
backend/
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── setup.cfg          # Contains flake8 settings 
├── task_flow_api      # Django settings and project config
└── tasks              # Tasks app
```

## Getting started

### Prerequisites
- Python 3.14+
- PostgreSQL 18.x
- [Poetry](https://python-poetry.org/) for dependency and virtual environment management

### Installation
Clone the repository / download code

Install dependencies with poetry and activate virtual environment:
```shell
poetry install
eval $(poetry env activate)
```

### Environment variables
Create a `.env` file at the root of the project or copy and rename the existing `example.env`

Set the following settings:
#### Django settings
- `SECRET_KEY` - A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
- `DEBUG` - A boolean that turns on/off debug mode. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).
- `ALLOWED_HOSTS` - A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations. [See details at Django docs.](https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts)
- `DATABASE_URL` - Database settings in form of a URL. See details at [dj-database-url docs](https://github.com/jazzband/dj-database-url/).

#### Simple JWT settings
- `ACCESS_TOKEN_LIFETIME` - Access token lifetime in minutes.
- `REFRESH_TOKEN_LIFETIME` - Refresh token lifetime in days.

### Database setup
Make sure PostgreSQL is running and has a table ready for the project. A simple way to set up PostgreSQL is to run it via Docker. Refer to [PostgreSQL's docs](https://www.postgresql.org/docs/18/tutorial-start.html) and/or Docker's [PostgreSQL image's page](https://hub.docker.com/_/postgres#how-to-use-this-image).

If doing via Docker:
```commandline
docker run --name taskflow-db -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:18
```
And set `DATABASE_URL` env setting to `postgres://postgres:postgres@localhost:5432/postgres`

After the database is up and running, run migrations:
```shell
python manage.py migrate
```

Create a superuser:
```shell
python manage.py createsuperuser
```

### Run the development server
Start it by running:

```shell
python manage.py runserver
```

The API is now available at `http://127.0.0.1:8000/` or `http://localhost:8000/`.  
See API docs further down for specific endpoints or go to `http://127.0.0.1:8000/api/docs/` for interactable API docs made with DRF Spectacular / Swagger UI.

## API documentation
Note: the examples of requests in this section are made with [httpie CLI](https://httpie.io/cli))

### Permissions
For every task endpoint authentication is required. Currently, session authentication through a web browser (e.g. by opening api root at `/api/` and clicking "Log in" button), but the main method is via JWT. Session authentication works only in browser-based DRF UI (or Django Admin) and is not intended for API clients.  
Once an access token is obtained (see Authentication endpoints below), it should be used with `Authorization` header as such:
```commandline
Authorization: Bearer <access_token>
```

Users can only access their own tasks and can only do so (as well as create new tasks) while being authenticated.

### Authentication endpoints

[//]: # (- `POST /api/users/register/` - create an account)
- `POST /api/token/` - obtain JWT tokens
- `POST /api/token/refresh/` - refresh access token

Note: currently, creating new users is only possible through Django Admin view at `/admin/` or `manage.py createsuperuser`. Will be remade into a proper endpoint in the future. 

Examples:

[//]: # (```commandline)

[//]: # (http POST http://127.0.0.1:8000/api/users/register/ username="new_user" password="secure_password_123")

[//]: # (```)

```commandline
$ http POST http://127.0.0.1:8000/api/token/ username="new_user" password="secure_password_123"

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....FbDeSsxv5nRdjpOvx0cxVRn-I",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....dasdSFdf1sIc8cEN35f2L1VXU"
}
```
```commandline
$ http POST http://127.0.0.1:8000/api/token/refresh/ refresh=<refresh_token>

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....-g2vyq-NPX5EhOFWRQ"
}
```

### Task endpoints

- `GET /api/tasks/` – list user’s tasks
- `POST /api/tasks/` – create new task
- `GET /api/tasks/<id>/` – retrieve a single task
- `PUT /api/tasks/<id>/` – update a task
- `PATCH /api/tasks/<id>/` – partially update a task
- `DELETE /api/tasks/<id>/` – delete a task

Examples:
```commandline
$ http GET http://127.0.0.1:8000/api/tasks/ Authorization:"Bearer <access_token>"

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "is_completed": true,
            "name": "example completed task",
            "owner": "username"
        },
        {
            "id": 1,
            "is_completed": false,
            "name": "example task",
            "owner": "username"
        }
    ]
}
```

```commandline
$ http POST http://127.0.0.1:8000/api/tasks/ Authorization:"Bearer <access_token>" name="another example task"

{
    "id": 3,
    "is_completed": false,
    "name": "another example task",
    "owner": "username"
}
```