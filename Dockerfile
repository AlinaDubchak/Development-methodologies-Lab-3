FROM python:3.10-alpine

RUN apk add --no-cache lapack-dev g++ gcc musl-dev

WORKDIR /app

# Dependancies
COPY requirements/backend.in .

RUN pip install --no-cache-dir -r backend.in

# Code
COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]