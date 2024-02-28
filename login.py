import streamlit as st

# Define correct login credentials
CORRECT_USERNAME = "user"
CORRECT_PASSWORD = "password"

def main():
    st.title("Login Page")

    # Add a sidebar
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Login", "About"])

    if page == "Login":
        st.header("Login")

        # Get username and password from user
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Check if username and password are correct
        if st.button("Login"):
            if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
                st.success("Login successful!")
                # Redirect to another page or perform other actions here
            else:
                st.error("Invalid username or password. Please try again.")
    elif page == "About":
        st.header("About")
        st.write("This is a simple login page example using Streamlit.")

if __name__ == "__main__":
    main()
