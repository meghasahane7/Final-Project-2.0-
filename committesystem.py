import streamlit as st
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('committee_system.db')
c = conn.cursor()

# Create a table to store committee members if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS members
             (id INTEGER PRIMARY KEY, committee TEXT, member TEXT)''')

# Function to add a member to a committee in the database
def add_member(committee, member):
    c.execute('''INSERT INTO members (committee, member) VALUES (?, ?)''',
              (committee, member))
    conn.commit()

# Function to remove a member from a committee in the database
def remove_member(committee, member):
    c.execute('''DELETE FROM members WHERE committee=? AND member=?''', (committee, member))
    conn.commit()

# Function to retrieve members of a committee from the database
def get_committee_members(committee):
    c.execute('''SELECT member FROM members WHERE committee=?''', (committee,))
    return [row[0] for row in c.fetchall()]

# Main function
def main():
    st.title("Committee System")

    st.sidebar.title("Add Member")
    new_committee = st.sidebar.text_input("Committee Name")
    new_member = st.sidebar.text_input("Member Name")
    if st.sidebar.button("Add"):
        add_member(new_committee, new_member)
        st.sidebar.success(f"Added {new_member} to {new_committee}")

    st.sidebar.title("Remove Member")
    remove_committee = st.sidebar.selectbox("Select Committee", [row[0] for row in c.execute('''SELECT DISTINCT committee FROM members''').fetchall()], 0)
    remove_member_name = st.sidebar.selectbox("Select Member", get_committee_members(remove_committee), 0)
    if st.sidebar.button("Remove"):
        remove_member(remove_committee, remove_member_name)
        st.sidebar.success(f"Removed {remove_member_name} from {remove_committee}")

    st.header("Committees and Members")
    for row in c.execute('''SELECT DISTINCT committee FROM members''').fetchall():
        committee = row[0]
        st.subheader(committee)
        members = get_committee_members(committee)
        for member in members:
            st.write(member)

if __name__ == "__main__":
    main()
