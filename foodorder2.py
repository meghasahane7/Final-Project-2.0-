import streamlit as st
import sqlite3
import os

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        st.error(e)
    return conn

# Function to create a table in the database if it does not exist
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Orders
                     (id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER)''')
    except sqlite3.Error as e:
        st.error(e)

# Function to insert order data into the database
def insert_order(conn, item, quantity):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO Orders (item, quantity) VALUES (?, ?)", (item, quantity))
        conn.commit()
        st.success("Order placed successfully!")
    except sqlite3.Error as e:
        st.error(e)

# Function to retrieve all orders from the database
def get_orders(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Orders")
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        st.error(e)

# Main function
def main():
    st.set_page_config(page_title="Food Order App", page_icon="🍔")
    st.title("Food Order App")
    conn = create_connection("orders.db")
    if conn is not None:
        create_table(conn)

        pages = ["Menu", "Order History"]
        page = st.sidebar.radio("Navigation", pages)

        if page == "Menu":
            menu_page(conn)
        elif page == "Order History":
            order_history_page(conn)

        conn.close()

# Function for displaying the menu page
def menu_page(conn):
    st.header("Menu")
    menu_items = {
        "Pizza": {"image": "pizza.png", "description": "Delicious pizza with various toppings."},
        "Burger": {"image": "burger.png", "description": "Juicy burger with cheese and fries."},
        "Pasta": {"image": "pasta.png", "description": "Tasty pasta with your choice of sauce."}
    }

    for item_name, item_info in menu_items.items():
        st.subheader(item_name)
        st.image(item_info["image"], caption=item_info["description"], width=200)

        quantity = st.number_input(f"Quantity of {item_name}", min_value=0, max_value=10, step=1)
        if quantity > 0:
            if st.button(f"Order {item_name}"):
                insert_order(conn, item_name, quantity)

# Function for displaying the order history page
def order_history_page(conn):
    st.header("Order History")
    orders = get_orders(conn)
    if orders:
        for order in orders:
            st.write(f"Item: {order[1]}, Quantity: {order[2]}")
    else:
        st.write("No orders yet.")

if __name__ == "__main__":
    main()
