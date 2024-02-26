import streamlit as st
import pandas as pd

# Create dataframes to store patient and appointment information
patients_df = pd.DataFrame(columns=["Name", "Age", "Gender", "Contact"])
appointments_df = pd.DataFrame(columns=["Patient Name", "Doctor", "Date", "Time"])

# Function to register a new patient
def register_patient(name, age, gender, contact):
    global patients_df
    patients_df = patients_df.append({"Name": name, "Age": age, "Gender": gender, "Contact": contact}, ignore_index=True)
    st.success("Patient registered successfully!")

# Function to schedule an appointment
def schedule_appointment(patient_name, doctor, date, time):
    global appointments_df
    appointments_df = appointments_df.append({"Patient Name": patient_name, "Doctor": doctor, "Date": date, "Time": time}, ignore_index=True)
    st.success("Appointment scheduled successfully!")

# Main function
def main():
    st.title("Hospital Management System")

    st.header("Patient Registration")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact = st.text_input("Contact Number")
    if st.button("Register"):
        register_patient(name, age, gender, contact)

    st.header("Appointment Scheduling")
    patient_name = st.selectbox("Select Patient", patients_df["Name"].tolist())
    doctor = st.text_input("Doctor")
    date = st.date_input("Date")
    time = st.time_input("Time")
    if st.button("Schedule"):
        schedule_appointment(patient_name, doctor, date, time)

    st.header("Patient Database")
    st.write(patients_df)

    st.header("Appointment Database")
    st.write(appointments_df)

if __name__ == "__main__":
    main()
