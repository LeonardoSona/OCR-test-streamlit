import streamlit as st
import easyocr
from PIL import Image

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

# Set up the title of the app
st.title("Image to Text Extractor")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image and display it
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR on the uploaded image
    result = reader.readtext(image)

    # Display the extracted text
    extracted_text = ""
    for (bbox, text, prob) in result:
        extracted_text += f"{text}\n"
    
    st.subheader("Extracted Text")
    st.text(extracted_text)
