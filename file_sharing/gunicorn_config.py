import os

workers = int(os.getenv('GUNICORN_WORKERS', os.cpu_count() * 2 + 1))
bind = os.getenv('GUNICORN_BIND', '0.0.0.0:8000')
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')