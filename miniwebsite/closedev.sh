#!bin/bash

echo "Deactivating virtual environment"
#deactivate's the virtual environment
source ../deactivate_venv
echo "Changing dir"

# stop the dev server from running
docker-compose stop