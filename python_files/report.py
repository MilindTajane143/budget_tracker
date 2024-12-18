import mysql.connector
import matplotlib.pyplot as plt

# Database connection setup
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # Change if your MySQL server is hosted elsewhere
        user="root",            # Replace with your MySQL username
        password="Milind@#2429",    # Replace with your MySQL password
        database="budget_tracker"
    )

# Function to generate a report
def generate_report(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch transactions grouped by category
        query = '''SELECT category, SUM(amount) 
                   FROM transactions 
                   WHERE user_id = %s AND type = 'Expense'
                   GROUP BY category'''
        cursor.execute(query, (user_id,))

        transactions = cursor.fetchall()

        if not transactions:
            print("No transactions found for the user to generate a report.")
            return

        # Prepare data for the pie chart
        categories = [t[0] for t in transactions]
        amounts = [t[1] for t in transactions]

        # Plot the pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title(f'Spending by Category for User ID: {user_id}')
        plt.show()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# Testing the report generation
if __name__ == "__main__":
    # Replace with an actual user ID from your `users` table
    user_id = 1  

    print(f"Generating report for User ID: {user_id}")
    generate_report(user_id)
