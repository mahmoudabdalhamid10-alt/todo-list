<picture><img src="https://github.com/user-attachments/assets/88148010-19f6-499a-a275-e0a80cda72ad" alt="Task Management App" width="100%" /></picture>

<h1 align="center">Task Management App</h1>

<p align="center"><strong>Full-stack task manager: a Flask REST API with JWT auth and a React 19 single-page frontend.</strong></p>

<p align="center">
<img src="https://img.shields.io/badge/Flask-0b1220?style=for-the-badge&logo=flask&logoColor=67e8f9" alt="Flask" />
<img src="https://img.shields.io/badge/React_19-0b1220?style=for-the-badge&logo=react&logoColor=67e8f9" alt="React 19" />
<img src="https://img.shields.io/badge/SQLAlchemy-0b1220?style=for-the-badge&logo=sqlalchemy&logoColor=67e8f9" alt="SQLAlchemy" />
<img src="https://img.shields.io/badge/JWT-0b1220?style=for-the-badge&logo=jsonwebtokens&logoColor=67e8f9" alt="JWT" />
<img src="https://img.shields.io/badge/Vite-0b1220?style=for-the-badge&logo=vite&logoColor=67e8f9" alt="Vite" />
</p>

<p align="center"><sub>Artwork is illustrative.</sub></p>

## What it does

- **Accounts**: register and log in with username/email; passwords hashed with bcrypt, sessions carried by JWT access tokens (1-day expiry, with clean 401/422 error responses).
- **Tasks**: full CRUD per user. Each task has a title, optional description, priority (`low` / `medium` / `high`), status (defaults to `Not started`), due date and optional reminder date.
- **Frontend**: React 19 + Vite SPA with login/signup forms, a dashboard with the task list, dark/light theme context, and toast notifications (react-toastify). API calls go through a small axios layer.
- **Backend structure**: application factory (`create_app`), blueprints (`/auth`, `/tasks`), Flask-SQLAlchemy models, Flask-Migrate (Alembic) migrations, marshmallow serialization, CORS enabled, `/health` endpoint.
- **Deployment configs included**: `render.yaml` (gunicorn + `flask db upgrade`) for the API and `vercel.json` (SPA rewrites) for the frontend.

## Tech stack

| Layer | Tools |
|---|---|
| Frontend | React 19, Vite 6, react-router 7, axios, Headless UI, react-toastify, SCSS |
| Backend | Flask 3, Flask-JWT-Extended, Flask-SQLAlchemy, Flask-Migrate, Flask-Bcrypt, marshmallow |
| Database | SQLite by default (PostgreSQL-ready via `SQLALCHEMY_DATABASE_URI`, psycopg2 included) |

## Run it locally

Backend (from the repo root):

```bash
pip install -r requirements.txt
flask db upgrade          # applies migrations/ to a local SQLite file
python wsgi.py            # serves the API, /health answers {"status": "healthy"}
```

Frontend:

```bash
npm install
npm run dev               # Vite dev server
```

Configuration is read from the environment: `SQLALCHEMY_DATABASE_URI` and
`JWT_SECRET_KEY`. Set your own `JWT_SECRET_KEY` before deploying anywhere -
the fallback in `app/config.py` is committed in the repo and must not be used
in production.

## API overview

| Endpoint | Methods | Purpose |
|---|---|---|
| `/auth/register` | POST | create account |
| `/auth/login` | POST | get a JWT |
| `/tasks` | GET, POST | list my tasks, create a task |
| `/tasks/<id>` | GET, PUT, DELETE | read / update / delete one task |
| `/health` | GET | liveness probe |

## Project layout

```
app/            Flask backend (factory, config, models, routes, migrations glue)
  auth/         JWT helpers
  models/       User and Tasks SQLAlchemy models
  routes/       auth and task blueprints
migrations/     Alembic migrations
src/            React frontend (pages, components, contexts, hooks, api layer)
wsgi.py         gunicorn entry point (used by render.yaml)
vercel.json     frontend SPA deployment
```
