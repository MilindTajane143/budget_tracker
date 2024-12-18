import tkinter as tk
from tkinter import messagebox
from user_auth import authenticate_user, register_user
from transaction import add_transaction, get_transactions
from report import generate_report
from budget import set_budget, get_budget

# Function to handle the user login
def login_window():
    def login():
        username = entry_username.get()
        password = entry_password.get()

        # Authenticate user
        user = authenticate_user(username, password)
        if user:
            messagebox.showinfo("Login", "Login successful!")
            root.destroy()  # Close the login window
            main_window(user[0])  # Pass the user ID to the main window
        else:
            messagebox.showerror("Login", "Invalid credentials. Please try again.")

    # Create the login window
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    entry_username = tk.Entry(login_window)
    entry_username.grid(row=0, column=1)

    tk.Label(login_window, text="Password:").grid(row=1, column=0)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(login_window, text="Login", command=login).grid(row=2, column=0, columnspan=2)

    login_window.mainloop()


# Main dashboard window after login
def main_window(user_id):
    def view_transactions():
        transactions = get_transactions(user_id)
        if not transactions:
            messagebox.showinfo("Transactions", "No transactions found.")
        else:
            transactions_window = tk.Toplevel(root)
            transactions_window.title("Transactions")
            
            for i, txn in enumerate(transactions):
                tk.Label(transactions_window, text=f"{txn[1]} - {txn[0]} - {txn[2]} - {txn[3]}").grid(row=i, column=0)

    def add_new_transaction():
        def save_transaction():
            amount = entry_amount.get()
            description = entry_description.get()
            category = entry_category.get()
            type_of_transaction = var_type.get()

            # Validate and add the transaction
            if not amount or not description or not category or not type_of_transaction:
                messagebox.showerror("Error", "All fields are required!")
                return

            add_transaction(user_id, float(amount), description, category, type_of_transaction)
            messagebox.showinfo("Success", "Transaction added successfully!")
            add_transaction_window.destroy()

        # Create the add transaction window
        add_transaction_window = tk.Toplevel(root)
        add_transaction_window.title("Add Transaction")

        tk.Label(add_transaction_window, text="Amount:").grid(row=0, column=0)
        entry_amount = tk.Entry(add_transaction_window)
        entry_amount.grid(row=0, column=1)

        tk.Label(add_transaction_window, text="Description:").grid(row=1, column=0)
        entry_description = tk.Entry(add_transaction_window)
        entry_description.grid(row=1, column=1)

        tk.Label(add_transaction_window, text="Category:").grid(row=2, column=0)
        entry_category = tk.Entry(add_transaction_window)
        entry_category.grid(row=2, column=1)

        tk.Label(add_transaction_window, text="Type:").grid(row=3, column=0)
        var_type = tk.StringVar()
        tk.Radiobutton(add_transaction_window, text="Income", variable=var_type, value="Income").grid(row=3, column=1)
        tk.Radiobutton(add_transaction_window, text="Expense", variable=var_type, value="Expense").grid(row=3, column=2)

        tk.Button(add_transaction_window, text="Save Transaction", command=save_transaction).grid(row=4, column=0, columnspan=3)

    def view_report():
        generate_report(user_id)  # Show report for user

    # Create the main window (Dashboard)
    root = tk.Tk()
    root.title("Budget Tracker Dashboard")

    tk.Button(root, text="View Transactions", command=view_transactions).pack(pady=10)
    tk.Button(root, text="Add New Transaction", command=add_new_transaction).pack(pady=10)
    tk.Button(root, text="View Spending Report", command=view_report).pack(pady=10)

    root.mainloop()

# Start the login window
login_window()
