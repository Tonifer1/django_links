#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Check if the superuser exists before attempting to create it
if [ $(echo "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists())" | python manage.py shell) == "False" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --no-input
else
    echo "Superuser already exists. Skipping creation."
fi