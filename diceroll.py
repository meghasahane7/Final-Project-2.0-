import streamlit as st
import random

def main():
    st.title("Dice Rolling Game")

    dice_sides = st.sidebar.selectbox("Select number of sides", [4, 6, 8, 10, 12, 20])

    if st.button("Roll Dice"):
        roll_result = random.randint(1, dice_sides)
        st.write(f"You rolled a {dice_sides}-sided dice and got: {roll_result}")

if __name__ == "__main__":
    main()
