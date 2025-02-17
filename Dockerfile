FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'file_sharing.settings'

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    netcat-openbsd

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY entrypoint.sh app/entrypoint.sh
RUN chmod +x  app/entrypoint.sh
COPY . .
COPY file_sharing/gunicorn_config.py /app/gunicorn_config.py

ENTRYPOINT ["app/entrypoint.sh"]
CMD ["sh", "-c", "gunicorn file_sharing.wsgi:application --config gunicorn_config.py"]