Rock vs Mine Prediction

📌 Project Overview

This project is a Machine Learning-based web application that predicts whether a given sonar reading corresponds to a Rock or a Mine. The model has been trained using Supervised Learning and is deployed using Streamlit.

🚀 Features

Upload sonar readings and get instant predictions.

Uses a trained Machine Learning model for accurate results.

Handles missing or incorrect data entries.

Simple and interactive Streamlit web interface.

Rock-Vs-Mine-Prediction/
│-- app.py                 # Streamlit web application
│-- rock_vs_mine_model.pkl # Trained Machine Learning model
│-- sonar data.csv         # Dataset used for training
│-- requirements.txt       # Dependencies required to run the project
│-- README.md              # Project documentation (this file)

📊 Dataset Information

The dataset consists of sonar signals with 60 numerical features.

Each row represents a sonar reading.

Labels: R (Rock) or M (Mine).

🖥️ Usage

Run the application using streamlit run app.py.

Enter 60 sonar values manually.

Click Predict to see whether the input corresponds to a Rock or a Mine.

The result is displayed instantly.

🔥 Technologies Used

Python

Pandas for data manipulation

Scikit-learn for ML model

Streamlit for deployment

Joblib for model serialization

🛠️ Troubleshooting

If you get a FileNotFoundError, make sure the model file (rock_vs_mine_model.pkl) is in the same directory as app.py.

If Streamlit fails to run, ensure all dependencies are installed properly using pip install -r requirements.txt.

This is a **Machine Learning Web Application** that predicts whether sonar readings correspond to **Rock** or **Mine**.  
The app is built using **Streamlit** and is deployed on Streamlit Cloud.

## 🚀 Live Demo
🔗 **[Try the Web App](https://rock-vs-mine-prediction-5y4kdbpk7aacwyxz5uliwx.streamlit.app/)**![Screenshot 2025-03-04 161404](https://github.com/user-attachments/assets/4c0b9b61-93e1-4611-bd87-0116fcee3c51)
