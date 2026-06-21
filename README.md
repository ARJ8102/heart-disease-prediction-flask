# HEART+ | Heart Disease Prediction System

HEART+ is a Flask-based machine learning web application that predicts the risk of heart disease based on patient health parameters. The project takes user input through a web form, processes the data, and uses a trained Random Forest model to generate a prediction.

This project was built as an end-to-end machine learning deployment project, covering data preprocessing, model training, web application development, GitHub version control, and cloud deployment using Render.

---

## Live Demo

Add your deployed Render link here:

```text
https://heart-disease-prediction-flask-evsj.onrender.com/

#################################################################################################################################

Project Overview

The goal of this project is to predict whether a patient is at high or low risk of heart disease using common clinical and health-related input features.

The app allows users to enter patient details such as age, gender, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, ECG results, maximum heart rate, exercise-induced angina, old peak, and ST slope.

Based on these inputs, the trained machine learning model returns a prediction:

High risk of heart disease
Low risk of heart disease

###############################################################################################################################

Features
User authentication with signup, login, and logout
Heart disease prediction form
Dropdown inputs for categorical medical parameters
Random Forest machine learning model
Flask backend for prediction handling
SQLite database for user accounts
Bootstrap-based frontend
Deployed online using Render

#################################################################################################################################
Tech Stack

Frontend
HTML
CSS
Bootstrap

Backend
Python
Flask
Flask-Login
Flask-WTF
Flask-SQLAlchemy

Machine Learning
pandas
NumPy
scikit-learn
Random Forest Classifier
Pickle model serialization

Deployment
GitHub
Render
Gunicorn

##############################################################################################################################

Dataset

The model was trained using a heart disease dataset containing patient health attributes such as:

Age
Sex
Chest pain type
Resting blood pressure
Cholesterol
Fasting blood sugar
Resting ECG
Maximum heart rate achieved
Exercise-induced angina
Old peak / ST depression
ST slope
Target value

The target column indicates whether heart disease risk is present or not.

#################################################################################################################################

Machine Learning Workflow
Loaded the heart disease dataset using pandas.
Renamed and cleaned dataset columns.
Split the data into features and target.
Divided the dataset into training and testing sets.
Trained a Random Forest Classifier.
Saved the trained model using Pickle.
Loaded the saved model inside the Flask app.
Used form input values to generate real-time predictions.

################################################################################################################################

Input Features
Feature	Description
Age	Patient age in years
Sex	Male or Female
Chest Pain Type	Type of chest pain experienced
Resting Blood Pressure	Resting blood pressure value
Cholesterol	Serum cholesterol level
Fasting Blood Sugar	Whether fasting blood sugar is greater than 120 mg/dl
Resting ECG	Resting electrocardiographic result
Maximum Heart Rate	Maximum heart rate achieved
Exercise Angina	Exercise-induced angina status
Old Peak	ST depression induced by exercise
ST Slope	Slope of the peak exercise ST segment

#################################################################################################################################

How to Run Locally

1. Clone the repository
git clone https://github.com/ARJ8102/heart-disease-prediction-flask
cd your-repository-name
2. Create and activate a virtual environment

For Windows:

python -m venv hdp
hdp\Scripts\activate

For macOS/Linux:

python3 -m venv hdp
source hdp/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the Flask app
python app.py
5. Open in browser
http://127.0.0.1:5000/

##################################################################################################################################

eployment

The application is deployed using Render.

Render deployment configuration:

Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

A Procfile is also included:

web: gunicorn app:app

##################################################################################################################################

Disclaimer

This project is created for educational and portfolio purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Users should consult a qualified healthcare professional for any medical concerns.