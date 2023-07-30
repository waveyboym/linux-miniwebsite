#!/bin/bash

# activate's the virtual environment
echo 'Building and running server for dev now...'
source ./activate_venv

# change directory
cd miniwebsite

# removing network and previous container
docker-compose down -v

# let docker build an image
docker-compose build

# let docker run the container
docker-compose up -d