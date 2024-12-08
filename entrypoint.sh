service ssh start

python manage.py migrate

redis-server \
    & python manage.py runserver "0.0.0.0:80" \
    & watchmedo auto-restart --patterns="*.py" --recursive -- celery -A project worker --loglevel=info \
    & wait -n

exec "$@"