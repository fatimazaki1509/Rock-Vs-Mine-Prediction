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

# Sidebar
st.sidebar.header("Enter 60 Features Manually")

# Create input fields for 60 features
features = []
for i in range(60):
    value = st.sidebar.number_input(f"Feature {i+1}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    features.append(value)

# Convert to NumPy array
features = np.array(features).reshape(1, -1)

# Predict Button
if st.sidebar.button("Predict"):
    prediction = model.predict(features)
    result = "Mine" if prediction[0] == 1 else "Rock"
    
    # Display Result
    st.write(f"### 🏆 Prediction: **{result}**")

# Footer
st.markdown("<h4 style='text-align: center;'>Powered by Machine Learning 🧠</h4>", unsafe_allow_html=True)










