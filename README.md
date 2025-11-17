# Module 11 – Calculation Model & CI/CD

This project implements a `Calculation` model using SQLAlchemy, Pydantic schemas for validation, an optional factory pattern for operations, and a CI/CD pipeline with GitHub Actions and Docker.

## 1. Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Running tests locally

By default, tests run against a local SQLite database:

```bash
pytest
```

To run tests against PostgreSQL via Docker:

```bash
docker compose up -d db
export TEST_DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/appdb
pytest
```

## 3. Running the app with Docker

```bash
docker compose up --build
```

Then visit: `http://localhost:8000/`

## 4. CI/CD with GitHub Actions

The workflow file is in `.github/workflows/ci.yml`.

On pushes to `main`:

1. Spins up a PostgreSQL service.
2. Installs dependencies.
3. Runs unit + integration tests.
4. Builds and pushes a Docker image to Docker Hub **if tests pass**.

You must set these GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Update the image tag in `ci.yml` to match your Docker Hub repo:

```yaml
tags: YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:latest
```

## 5. Docker Hub

Once CI passes, your image will be available on Docker Hub under the repo name you configure in the workflow.
