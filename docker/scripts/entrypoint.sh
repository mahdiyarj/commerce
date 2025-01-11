#!/bin/bash

./wait-for-it.sh db:5432 --timeout=60 --strict -- echo "Database is up"

echo "Applying database migrations..."
python manage.py migrate

echo "Checking for existing Django superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password')
else:
    print('Superuser already exists.')
EOF


echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000