import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="db",
    database="mydb",
    user="myuser",
    password="mypassword"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a SELECT statement to fetch all messages from the messages table
cur.execute("SELECT * FROM messages")

# Fetch all the rows and print them
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and the database connection
cur.close()
conn.close()