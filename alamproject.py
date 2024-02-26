import streamlit as st
import time
from datetime import datetime

# Function to check if the current time matches the alarm time
def check_alarm(alarm_time):
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        return True
    else:
        return False

def main():
    st.title("Alarm Clock")

    alarm_time = st.time_input("Set Alarm Time")
    alarm_time_str = alarm_time.strftime("%H:%M:%S")
    st.write(f"Alarm set for: {alarm_time_str}")

    if st.button("Start Alarm"):
        while True:
            if check_alarm(alarm_time_str):
                st.success("Alarm! Wake up!")
                break
            else:
                time.sleep(1)

if __name__ == "__main__":
    main()
