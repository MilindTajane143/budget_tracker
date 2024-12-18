import mysql.connector

def set_budget(user_id, category, limit):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="budget_tracker_db"
    )
    cursor = conn.cursor()

    # Insert the budget data
    cursor.execute(
        "INSERT INTO budgets (user_id, category, limit) VALUES (%s, %s, %s)",
        (user_id, category, limit)
    )
    conn.commit()
    conn.close()

def get_budget(user_id, category):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="budget_tracker_db"
    )
    cursor = conn.cursor()

    # Retrieve the budget data
    cursor.execute(
        "SELECT limit FROM budgets WHERE user_id = %s AND category = %s",
        (user_id, category)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]  # Return the budget limit
    else:
        return None  # No budget found
