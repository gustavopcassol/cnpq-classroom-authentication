#!/bin/sh

# If backend container was created with a different name, change this.
container=cnpq-classroom-authentication_backend_1

# Commands
exec="docker exec ${container}"
manage="${exec} python manage.py"

# Django
echo Starting migrate...
$manage migrate
echo Collecting static files...
$manage collectstatic --no-input
