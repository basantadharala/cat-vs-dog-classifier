import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('cat_dog_classifier_kaggle1.h5')


# Function to preprocess the uploaded image
def preprocess_image(image):
    image = image.convert('RGB')  # Ensure the image is in RGB mode
    image = image.resize((256, 256))  # Resize to the input shape of the model
    image = np.array(image)
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


# Function to make predictions
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    confidence = prediction[0][0]
    label = 'Dog' if confidence > 0.5 else 'Cat'
    confidence = confidence if label == 'Dog' else 1 - confidence
    return label, confidence


# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        color: white;
        background-color: #007BFF;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stTextArea>div>textarea {
        height: 150px;
    }
    .stImage>div {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit interface
st.title('🐱🐶 Cat or Dog Classifier 🐱🐶')
st.write("Upload an image to classify whether it's a cat or a dog.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("")
    st.write("Classifying...")

    label, confidence = predict(image)

    st.write(f'The image is classified as a **{label}**.')
    st.write(f'**Confidence**: {confidence:.2f}')

    # Display progress bar for effect
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)
else:
    st.write("Please upload an image to get started.")

st.write("")
st.markdown("Developed by [Basanta Dharala](https://www.linkedin.com/in/basanta-dharala) | [GitHub](https://github.com/basantadharala)", unsafe_allow_html=True)
