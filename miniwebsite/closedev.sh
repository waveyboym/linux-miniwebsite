#!bin/bash

echo "Deactivating virtual environment"
# change to go up a directory
cd ..

#deactivate's the virtual environment
deactivate

# stop the dev server from running
docker-compose stop

# remove container and previous network
docker-compose down -v