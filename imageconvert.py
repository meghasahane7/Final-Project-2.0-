import streamlit as st
from PIL import Image
import io

# Function to convert image format
def convert_image_format(image, format):
    img_io = io.BytesIO()
    image.save(img_io, format=format)
    return img_io.getvalue()

# Function to check if the user is on a certain page
def is_on_page(session_state, page):
    return session_state.page == page

# Define SessionState class
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Streamlit UI
def main():
    st.sidebar.title("Main Menu")
    page = st.sidebar.radio("Go to", ["Home","About Us","Contact","Converter"])

    session_state = SessionState(page=page)

    # Company logo
    st.image("logo.png", use_column_width=True)

    if page == "Home":
        st.title("Welcome Bano Qabil to Image Converter")
        st.write("This is the home page.")

    elif page == "About Us":
        st.title("Project Description")
        st.write("Complete Details required about project.") 
    elif page == "Contact":
        st.title("Group Leader")
        st.write("contact and Email Address.") 
    elif page == "Converter":
        st.title("Image Converter")
        st.write("Upload an image and choose the output format.")

        # Upload image
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "gif"])

        if uploaded_file is not None:
            # Read image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Choose output format
            output_format = st.selectbox("Select output format", ["JPG", "PNG", "GIF"])

            # Convert and display converted image
            if st.button("Convert"):
                if output_format == "JPG":
                    converted_image = convert_image_format(image, "JPEG")
                    st.image(converted_image, caption="Converted Image", use_column_width=True)
                elif output_format == "PNG":
                    converted_image = convert_image_format(image, "PNG")
                    st.image(converted_image, caption="Converted Image", use_column_width=True)
                elif output_format == "GIF":
                    converted_image = convert_image_format(image, "GIF")
                    st.image(converted_image, caption="Converted Image", use_column_width=True)

if __name__ == "__main__":
    main()
