import os
import psycopg2
from flask import Flask, request

# Create Flask application
app = Flask(__name__)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname=os.environ['POSTGRES_DB'],
    user=os.environ['POSTGRES_USER'],
    password=os.environ['POSTGRES_PASSWORD'],
    host='db'
)

# Create table for storing messages
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, text TEXT)")
conn.commit()
cur.close()
conn.close()

# Create route for receiving POST requests to store messages
@app.route('/messages', methods=['POST'])
def create_message():
    message = request.json['message']
    conn = psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='db'
    )

# Insert message into database
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (text) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()

# Return success message
    return 'Message created\n'

if __name__ == '__main__':
# Run Flask application
    app.run(debug=True, host='0.0.0.0')