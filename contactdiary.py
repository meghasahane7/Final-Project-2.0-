import streamlit as st
import sqlite3

# Function to create SQLite database and table
def create_database():
    conn = sqlite3.connect('contact_diary.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to add a contact
def add_contact(name, phone, email):
    conn = sqlite3.connect('contact_diary.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    conn.close()

# Function to retrieve all contacts
def get_contacts():
    conn = sqlite3.connect('contact_diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Function to display add contact page
def add_page():
    st.title('Add Contact')
    st.sidebar.image('logo.png', use_column_width=True)  # Change 'your_company_logo.png' to the path of your logo
    name = st.text_input('Name')
    phone = st.text_input('Phone')
    email = st.text_input('Email')
    if st.button('Add'):
        add_contact(name, phone, email)
        st.success('Contact added successfully.')

# Function to display view contacts page
def view_page():
    st.title('View Contacts')
    st.sidebar.image('logo.png', use_column_width=True)  # Change 'your_company_logo.png' to the path of your logo
    contacts = get_contacts()
    if contacts:
        st.write("Current Contacts:")
        for contact in contacts:
            st.write(contact)
    else:
        st.write("No contacts available.")

# Main function to run the Streamlit app
def main():
    create_database()
    pages = {
        "Add Contact": add_page,
        "View Contacts": view_page
    }
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
