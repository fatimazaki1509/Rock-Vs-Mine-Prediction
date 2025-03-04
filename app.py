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
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background Image (Deep Sea Sonar Theme)
set_bg("https://cdn.pixabay.com/photo/2017/08/30/07/51/sea-2697736_1280.jpg")

# Load the trained model
model = joblib.load("rock_vs_mine_model.pkl")

# Header with Banner Image
st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Rock-Mine_Prediction_Banner.png", use_container_width=True)

# Title with Styling
st.markdown("<h1 style='text-align: center; color: white;'>Rock vs Mine Prediction</h1>", unsafe_allow_html=True)

# Sidebar with Logo
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/2/27/Underwater_Radar_Logo.png", width=150)
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




