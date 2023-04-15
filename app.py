import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for handling GET requests to the /messages endpoint
@app.route('/messages', methods=['GET'])
def get_messages():
    conn = psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='db'
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages")
    rows = cur.fetchall()
    messages = [{'id': row[0], 'text': row[1]} for row in rows]
    cur.close()
    conn.close()
    return {'messages': messages}

# Define a route for handling POST requests to the /messages endpoint
@app.route('/messages', methods=['POST'])
def create_message():
    message = request.json['message']
    conn = psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='db'
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (text) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()
    return 'Message created\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')