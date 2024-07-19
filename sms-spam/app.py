import streamlit as st
import subprocess
import sys

# Function to install a package using pip
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Attempt to import sklearn and install if not found
try:
    import sklearn
except ImportError:
    st.write("`scikit-learn` is not installed. Installing now...")
    install_package('scikit-learn')
    import sklearn  # Retry import after installation

import pickle

# Load the trained model and vectorizer
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Function to classify email
def classify_email(email_text):
    prediction = model.predict([email_text])
    return prediction[0]

# Streamlit app
st.title('Email Spam Classifier')

st.write("""
    This app classifies emails as spam or ham.
    Enter the email content below and click the "Classify" button to get the prediction.
""")

# Input from the user
email_text = st.text_area("Enter the email content here:")

# Button to classify the email
if st.button('Classify'):
    if email_text:
        prediction = classify_email(email_text)
        st.write(f"The email is classified as: **{prediction}**")
    else:
        st.write("Please enter some email content to classify.")
