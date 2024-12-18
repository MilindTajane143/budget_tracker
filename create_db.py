import mysql.connector

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Milind@#2429",  # Replace with your MySQL password
        database="budget_tracker"
    )
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL)''')

    # Create transactions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user_id INT,
                        amount DECIMAL(10, 2),
                        description TEXT,
                        category VARCHAR(255),
                        date DATETIME,
                        type VARCHAR(50),
                        FOREIGN KEY (user_id) REFERENCES users(id))''')

    # Create budgets table (fix for the `limit` keyword issue)
    cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user_id INT,
                        category VARCHAR(255),
                        `limit` DECIMAL(10, 2),  -- Escaping the keyword
                        FOREIGN KEY (user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()

create_db()
