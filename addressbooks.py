import streamlit as st
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# Create a table to store contacts if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)''')
conn.commit()

# Function to add a contact to the database
def add_contact(name, phone, email):
    c.execute('''INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)''',
              (name, phone, email))
    conn.commit()

# Function to delete a contact from the database
def delete_contact(name):
    c.execute('''DELETE FROM contacts WHERE name=?''', (name,))
    conn.commit()

# Function to search for a contact in the database
def search_contact(name):
    c.execute('''SELECT * FROM contacts WHERE name=?''', (name,))
    return c.fetchone()

# Function to display all contacts from the database
def display_contacts():
    c.execute('''SELECT * FROM contacts''')
    return c.fetchall()

# Main function
def main():
    st.title("Address Book")

    st.sidebar.title("Add Contact")
    name = st.sidebar.text_input("Name")
    phone = st.sidebar.text_input("Phone")
    email = st.sidebar.text_input("Email")

    if st.sidebar.button("Add Contact"):
        add_contact(name, phone, email)
        st.sidebar.success("Contact added successfully.")

    st.sidebar.title("Delete Contact")
    delete_name = st.sidebar.text_input("Name to delete")
    if st.sidebar.button("Delete Contact"):
        delete_contact(delete_name)
        st.sidebar.success("Contact deleted successfully.")

    st.sidebar.title("Search Contact")
    search_name = st.sidebar.text_input("Name to search")
    if st.sidebar.button("Search Contact"):
        contact = search_contact(search_name)
        if contact:
            st.write(f"Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
        else:
            st.error("Contact not found.")

    st.header("All Contacts")
    contacts = display_contacts()
    if contacts:
        for contact in contacts:
            st.write(f"Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
    else:
        st.info("No contacts in the address book.")

if __name__ == "__main__":
    main()
