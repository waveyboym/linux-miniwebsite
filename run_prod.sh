#!/bin/bash


# activate's the virtual environment
echo 'Building and running server now for prod...'
source ./activate_venv

# This command will basically remove the container and network from the previous build. If you did not, ignore this step and go to the next one
docker-compose -f docker-compose.prod.yml down -v

# This command will build the image
docker-compose -f docker-compose.prod.yml up -d --build

# This command will migrate
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput