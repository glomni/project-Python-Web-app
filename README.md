# Prerequisites:
Docker & Docker Compose installed on your local machine

# Clone the repository:
git clone https://github.com/glomni/demo_project_Virta.git

# Build Docker Python web server image:
docker-compose build

# Start Docker containers:
docker-compose up   

# Post messages to /messages endpoint which will insert it in the DB:
curl -X POST -H "Content-Type: application/json" -d '{"message": "<any_message>"}' http://localhost:8080/messages

# List all mesages in the DB:
docker ps --filter "name=demo_project_virta-web-1" //copy the container ID and add it to the next command

docker exec <container d> python list_messages.py

# Test GET method:
curl http://localhost:8080/messages
