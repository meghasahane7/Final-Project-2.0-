import streamlit as st
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('jobs.db')
c = conn.cursor()

# Create a table to store job listings if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS jobs
             (id INTEGER PRIMARY KEY, title TEXT, company TEXT, location TEXT, description TEXT)''')

# Function to add a job listing to the database
def add_job(title, company, location, description):
    c.execute('''INSERT INTO jobs (title, company, location, description) VALUES (?, ?, ?, ?)''',
              (title, company, location, description))
    conn.commit()

# Function to retrieve job listings from the database
def get_jobs(location):
    if location == "All":
        c.execute('''SELECT * FROM jobs''')
    else:
        c.execute('''SELECT * FROM jobs WHERE location=?''', (location,))
    return c.fetchall()

# Function to display job listings
def show_jobs(jobs):
    for job in jobs:
        st.write(f"**{job[1]}**")
        st.write(f"Company: {job[2]}")
        st.write(f"Location: {job[3]}")
        st.write(f"Description: {job[4]}")
        st.write("")

# Main function
def main():
    st.title("Job Portal")
    
    location = st.sidebar.selectbox("Select Location", ["All", "New York", "San Francisco", "Seattle"])
    
    filtered_jobs = get_jobs(location)
    
    show_jobs(filtered_jobs)
    
    st.sidebar.title("Add a Job")
    new_title = st.sidebar.text_input("Title")
    new_company = st.sidebar.text_input("Company")
    new_location = st.sidebar.text_input("Location")
    new_description = st.sidebar.text_area("Description")
    
    if st.sidebar.button("Add Job"):
        add_job(new_title, new_company, new_location, new_description)
        st.sidebar.success("Job added successfully!")
        
if __name__ == "__main__":
    main()
