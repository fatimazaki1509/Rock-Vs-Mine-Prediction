import streamlit as st
import pandas as pd
import joblib
import time

# ✅ Load the trained model
try:
    model = joblib.load("rock_vs_mine_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found! Make sure 'rock_vs_mine_model.pkl' is in the same folder as this script.")
    st.stop()  # Stop execution if model is missing

# Title with Styling
st.markdown("<h1 style='text-align: center;'>Rock vs Mine Prediction</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Upload your CSV file for prediction.")

# File Upload Section
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    data = pd.read_csv(uploaded_file)

    # ✅ Ensure data is numeric and has 60 columns
    if data.shape[1] == 60:
        st.success("✅ File Uploaded Successfully!")

        # Convert all values to numeric (force conversion, replacing errors)
        data = data.apply(pd.to_numeric, errors="coerce")

        # Fill missing values with 0
        data = data.fillna(0)

        # Animated Loading Effect
        with st.spinner("Analyzing the data... ⏳"):
            time.sleep(3)  # Simulating processing time

            try:
                predictions = model.predict(data)

                # Convert numerical predictions to labels
                results = ["Mine" if pred == 1 else "Rock" for pred in predictions]

                # Display Predictions
                st.write("### Prediction Results:")
                result_df = pd.DataFrame({"Prediction": results})
                st.dataframe(result_df)

            except ValueError as e:
                st.error(f"⚠️ Model Prediction Error: {e}")

    else:
        st.error("❌ Uploaded file must have exactly 60 columns.")

# Footer
st.markdown("<h4 style='text-align: center;'>Powered by Machine Learning 🧠</h4>", unsafe_allow_html=True)







