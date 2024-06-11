# 🐱🐶 Cat or Dog Classifier 🐱🐶
This is a Streamlit web application that classifies images as either a cat or a dog using a pre-trained TensorFlow model. The model is downloaded from Google Drive if it does not exist locally.

## Table of Contents
Demo
Features
Installation
Usage
File Structure
Technologies Used
Acknowledgements
License
Demo
You can try the live demo here.

## Features
Upload an image to classify whether it is a cat or a dog.
Displays the uploaded image and the classification result with confidence.
Custom CSS styling for the Streamlit interface.
## Installation
Prerequisites
Python 3.7 or higher
Streamlit
TensorFlow
gdown
## Clone the Repository

git clone https://github.com/yourusername/cat-vs-dog-classifier.git
cd cat-vs-dog-classifier
## Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
## Install Dependencies
pip install -r requirements.txt

## Running the App

streamlit run app.py
## How It Works
Upload an Image: Use the file uploader to select an image from your computer.
Image Display: The uploaded image will be displayed on the web page.
Classification: The app will classify the image as either a cat or a dog and display the result along with the confidence level.
File Structure
bash
Copy code
cat-vs-dog-classifier/
│
├── app.py                      # Main application file
├── requirements.txt            # Python dependencies
├── cat_dog_classifier_kaggle1.h5  # Trained model file
└── README.md                   # Project README file
## Technologies Used
Streamlit
TensorFlow
Python
PIL (Python Imaging Library)
gdown
## Acknowledgements
The pre-trained model is downloaded from Google Drive.
This project was developed by Basanta Dharala.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

