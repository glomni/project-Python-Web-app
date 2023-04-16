# Prerequisites:
Docker & Docker Compose installed on your local machine

# Clone the repository:
git clone https://github.com/glomni/demo_project_Virta.git

# Build Docker Python web server image:
docker-compose build

# Start Docker containers:
docker-compose up   

# Post messages to the /messages endpoint which will insert it into the DB (bash terminal):
./write_message.sh <type_your_message>

# List all mesages in the DB (bash terminal):
./list_messages.sh

# Test GET method:
curl http://localhost:8080/messages
