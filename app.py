import streamlit as st
import numpy as np
import joblib

# Load the trained model
try:
    model = joblib.load("rock_vs_mine_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found! Make sure 'rock_vs_mine_model.pkl' is in the same folder as this script.")
    st.stop()

# App Title
st.markdown("<h1 style='text-align: center;'>Rock vs Mine Prediction</h1>", unsafe_allow_html=True)

# Input Box for All 60 Features
st.sidebar.header("Enter 60 Features (comma-separated)")
user_input = st.sidebar.text_area("Paste values here (comma-separated)", "0.02,0.03,0.04,...,0.01")  # Example placeholder

# Predict Button
if st.sidebar.button("Predict"):
    try:
        # Convert input into a NumPy array
        features = np.array([float(x) for x in user_input.split(",")])

        # Check if exactly 60 values are entered
        if len(features) != 60:
            st.error(f"❌ Please enter exactly 60 values! You entered {len(features)} values.")
        else:
            features = features.reshape(1, -1)  # Reshape for model input
            prediction = model.predict(features)
            result = "Mine" if prediction[0] == 1 else "Rock"
            
            # Display Result
            st.write(f"### 🏆 Prediction: **{result}**")
    except ValueError:
        st.error("❌ Invalid input! Make sure you enter 60 numeric values separated by commas.")

# Footer
st.markdown("<h4 style='text-align: center;'>Powered by Machine Learning 🧠</h4>", unsafe_allow_html=True)











