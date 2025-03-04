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

# Set Background Image (Your Selected Image)
set_bg("https://t3.ftcdn.net/jpg/05/65/44/22/360_F_565442263_5aWSeBztZVh6MKaPE1mjtiJPxbqhqWl1.jpg")

# Load the trained model
model = joblib.load("rock_vs_mi





