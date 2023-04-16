#!/bin/bash

# Usage: ./write_message.sh <type_your_message>

curl -X POST -H "Content-Type: application/json" -d '{"message": "'${1}'"}' http://localhost:8080/messages