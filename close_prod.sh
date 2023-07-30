#!bin/bash

echo "Deactivating virtual environment"
#deactivate's the virtual environment
deactivate

# stop the prod server from running
docker-compose -f docker-compose.prod.yml stop

# This command will basically remove the container and network.
docker-compose -f docker-compose.prod.yml down -v
