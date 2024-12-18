import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Milind@#2429",
        database="budget_tracker"
    )

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    conn.close()
    return user
