import streamlit as st
import pickle

# Load the trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the vectorizer if needed
with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

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
