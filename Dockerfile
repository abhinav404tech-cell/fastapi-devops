# Use an official Python runtime as parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install OS deps required by asyncpg / build (kept minimal)
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY backend/ .

# Expose port uvicorn will run on
EXPOSE 8000

# Run the app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["sh","-c","uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
