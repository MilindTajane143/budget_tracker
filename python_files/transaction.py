import mysql.connector
import datetime

# Database connection setup
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # Change if your MySQL server is hosted elsewhere
        user="root",            # Replace with your MySQL username
        password="Milind@#2429",    # Replace with your MySQL password
        database="budget_tracker"
    )

# Function to add a transaction
def add_transaction(user_id, amount, description, category, type_of_transaction):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = '''INSERT INTO transactions (user_id, amount, description, category, date, type) 
                   VALUES (%s, %s, %s, %s, %s, %s)'''
        values = (user_id, amount, description, category, date, type_of_transaction)

        cursor.execute(query, values)
        conn.commit()

        print(f"Transaction added: {description} (${amount}) - {category} [{type_of_transaction}]")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# Function to fetch transactions for a user
def get_transactions(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = '''SELECT amount, description, category, date, type 
                   FROM transactions 
                   WHERE user_id = %s'''
        cursor.execute(query, (user_id,))

        transactions = cursor.fetchall()
        return transactions
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        conn.close()

# Testing the functions
if __name__ == "__main__":
    # Replace with an actual user ID from your `users` table
    user_id = 1  

    # Add sample transactions
    add_transaction(user_id, 150.75, "Grocery shopping", "Food", "Expense")
    add_transaction(user_id, 2000.00, "Salary credited", "Income", "Income")
    add_transaction(user_id, 300.00, "Gym membership", "Health", "Expense")

    # Fetch and display transactions
    transactions = get_transactions(user_id)
    print("\nTransactions for User ID:", user_id)
    for txn in transactions:
        print(f"Amount: {txn[0]}, Description: {txn[1]}, Category: {txn[2]}, Date: {txn[3]}, Type: {txn[4]}")
