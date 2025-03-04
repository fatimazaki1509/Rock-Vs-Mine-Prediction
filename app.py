import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("rock_vs_mine_model.pkl")

# Streamlit UI
st.title("Rock vs Mine Prediction App")
st.write("Upload a CSV file with 60 sonar readings per row to predict Rock or Mine.")

# File Upload
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    data = pd.read_csv(uploaded_file)
    
    # Ensure it has 60 features
    if data.shape[1] == 60:
        # Make predictions
        predictions = model.predict(data)

        # Convert numerical predictions to labels
        results = ["Mine" if pred == 1 else "Rock" for pred in predictions]

        # Display predictions
        st.write("Predictions:")
        result_df = pd.DataFrame({"Prediction": results})
        st.dataframe(result_df)

    else:
        st.error("Uploaded file must have exactly 60 columns.")
