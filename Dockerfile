FROM python:3.12-slim

# Accept an environment arg to help identify env-specific config
ARG ENVIRONMENT=dev
ENV DJANGO_ENV=$ENVIRONMENT
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install poetry

# Copy only dependencies first (cache layer)
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

# Copy the entire app source
COPY . /app/

# Don’t try to copy .env — let Compose provide it
# Don't do this: COPY .env.${ENVIRONMENT} .env

# Default command (can be overridden)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
