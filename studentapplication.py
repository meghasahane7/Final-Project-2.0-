import streamlit as st
import pandas as pd

# Function to display home page
def home():
    st.title("Welcome to Student Admission Portal")
    st.write("This portal allows you to apply for admission.")

 # Display company logo
    st.image("logo.png", use_column_width=True)

# Function to display admission form
def admission_form():
    st.title("Admission Form")
    st.write("Fill out the form to apply for admission.")

    # Your admission form code goes here
# Create form for user input
    with st.form(key='admission_form'):
        st.header("Personal Information")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=150, step=1)
        grade = st.selectbox("Grade", options=["9", "10", "11", "12"])

        st.header("Contact Information")
        email = st.text_input("Email")

        # Submit button
        submitted = st.form_submit_button("Submit")

        if submitted:
            # Data validation
            if not name or not email:
                st.error("Name and email are required fields.")
                return

            # Create dataframe to store data
            data = {
                'Name': [name],
                'Age': [age],
                'Grade': [grade],
                'Email': [email]
            }
            df = pd.DataFrame(data)

            # Save data to CSV file
            df.to_csv("admission_data.csv", mode='a', index=False, header=not st.session_state.data_exists)
            st.success("Application submitted successfully!")

            # Reset form fields
            st.session_state.data_exists = True
            st.session_state.name = ""
            st.session_state.age = ""
            st.session_state.grade = ""
            st.session_state.email = ""
if __name__ == "__main__":
    if 'data_exists' not in st.session_state:
        st.session_state.data_exists = False
    
# Function to display contact page
def contact():
    st.title("Contact Us")
    st.write("If you have any questions, feel free to contact us.")

# Function to display about page
def about():
    st.title("About Us")
    st.write("Learn more about our institution and admission process.")

# Main function to run the app
def main():
    #st.sidebar.title("Navigation")
    st.sidebar.image("logo.png", use_column_width=True)

    page = st.sidebar.selectbox("Go to", ["Home", "Admission Form", "Contact Us", "About Us"])

    if page == "Home":
        home()
    elif page == "Admission Form":
        admission_form()
    elif page == "Contact Us":
        contact()
    elif page == "About Us":
        about()

if __name__ == "__main__":
    main()
