#!/bin/bash

# activate's the virtual environment
echo 'Building and running server for dev now...'

# create a new virtual environment
echo 'creating virtual environment now...'
python3 -m venv miniwebsite_venv

# activate virtual environment
echo 'activating virtual environment...'
source miniwebsite_venv/bin/activate

# change directory
echo 'changing directory to /miniwebsite'
cd miniwebsite

# removing network and previous container
docker-compose down -v

# let docker build an image
docker-compose build

# let docker run the container
docker-compose up -d