FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIPENV_VENV_IN_PROJECT=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-traditional \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

# Copy project files
COPY . .

# Make scripts executable
RUN chmod +x docker/scripts/entrypoint.sh \
    docker/scripts/wait-for-it.sh

# Expose port 8000
EXPOSE 8000

# Set entrypoint
CMD ["./docker/scripts/entrypoint.sh"]