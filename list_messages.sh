#!/bin/bash

# Get the ID of the demo_project_virta-web-1 container
container_id=$(docker ps --filter "name=demo_project_virta-web-1" --format "{{.ID}}")

# List all messages in the database by running the list_messages.py script inside the container
docker exec $container_id python list_messages.py