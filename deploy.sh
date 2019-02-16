#!/bin/bash

cd travel
echo "Model migrations"
python manage.py makemigrations
python manage.py migrate

echo "load admin user"
python manage.py loaddata booking/fixtures/users.json

echo "run server"
python manage.py runserver 0.0.0.0:8000
