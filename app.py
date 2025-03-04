import streamlit as st
import pandas as pd
import joblib
import time

# Function to set a background image
def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{https://navalpost.com/wp-content/uploads/2021/05/Submerged_submarine.jpg}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background Image (Replace with your image URL or file path)
set_bg("https://navalpost.com/wp-content/uploads/2021/05/Submerged_submarine.jpg")  # Change this!

# Load the trained model
model = joblib.load("rock_vs_mine_model.pkl")

# Header with Image
st.image("rock_vs_mine_banner.png", use_column_width=True)  # Change this!

# Title with Styling
st.markdown("<h1 style='text-align: center; color: white;'>Rock vs Mine Prediction</h1>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.image("rock_vs_mine_logo.png", width=150)  # Change this!
st.sidebar.title("Navigation")
st.sidebar.markdown("Upload your CSV file for prediction.")

# File Upload Section
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    data = pd.read_csv(uploaded_file)

    # Ensure it has 60 features
    if data.shape[1] == 60:
        st.success("✅ File Uploaded Successfully!")
        
        # Animated Loading Effect
        with st.spinner("Analyzing the data... ⏳"):
            time.sleep(3)  # Simulating processing time
            predictions = model.predict(data)

        # Convert numerical predictions to labels
        results = ["Mine" if pred == 1 else "Rock" for pred in predictions]

        # Display Predictions
        st.write("### Prediction Results:")
        result_df = pd.DataFrame({"Prediction": results})
        st.dataframe(result_df)

    else:
        st.error("❌ Uploaded file must have exactly 60 columns.")

# Footer
st.markdown("<h4 style='text-align: center; color: white;'>Powered by Machine Learning 🧠</h4>", unsafe_allow_html=True)
