#!bin/bash

echo "Deactivating virtual environment"
#deactivate's the virtual environment
deactivate

# stop the prod server from running
docker-compose -f docker-compose.prod.yml stop