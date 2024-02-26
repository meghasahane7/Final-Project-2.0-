import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.title("Password Generator")

    length = st.slider("Select password length", 6, 30, 12)

    use_uppercase = st.checkbox("Include Uppercase Letters")
    use_numbers = st.checkbox("Include Numbers")
    use_special = st.checkbox("Include Special Characters")

    if st.button("Generate Password"):
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        st.success("Your generated password is: ")
        st.write(password)

if __name__ == "__main__":
    main()
