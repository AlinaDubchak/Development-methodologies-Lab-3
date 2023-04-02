FROM python:3.11.2-bullseye



WORKDIR /app

# Dependancies
COPY requirements/backend.in .

RUN pip install --no-cache-dir -r backend.in

# Code
COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]