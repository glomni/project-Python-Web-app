from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_message():
    content = request.json['content']
    conn = psycopg2.connect(
        host="db",
        database="messages",
        user="postgres",
        password="example")
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
    conn.commit()
    cur.close()
    conn.close()
    return 'Message added to database: %s\n' % content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')