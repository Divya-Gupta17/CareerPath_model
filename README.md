Career Path Recommendation System
Project Overview

The Career Path Recommendation System is an AI-powered web application designed to help students and professionals discover optimal career paths based on their skills, education, interests, and job experience. The system leverages Machine Learning from sklearn.linear_model import LogisticRegression
 to provide personalized career recommendations, along with course suggestions and guidance to enhance employability.

Features

Career Recommendations:

Predicts suitable career options based on candidate inputs such as academic scores, skills, interests, and gender.

Course Recommendations:

Suggests relevant online courses to strengthen skills required for the recommended careers.

Chatbot Integration (SkillBot):

Provides conversational guidance to users about career options, pathways.

Interactive Web Interface:

Developed using Flask (backend) and htl,css and js (frontend).

Users can input details via forms and receive immediate recommendations.

Database Integration:

Stores candidate inputs and recommended pathways for future reference and analytics.

Project Architecture
CareerPath/
│
├─ backend/
│   ├─ app.py                  # Main Flask backend application
│   ├─ Models/
│   │   ├─ career_model.pkl    # Trained ML model for career recommendations
│   │   ├─ label_encoders.pkl  # Encoders for categorical variables
│   │   └─ career_data.csv     # Dataset used for training
│   ├─ templates/
│   │   ├─ index.html          # Homepage
│   │   ├─ career.html         # Career recommendation page
│   │   ├─ courses.html        # Course recommendations page
│   │   ├─ chatbot.html        # Chatbot interface
│   │   └─ recommend.html      # Result display page
│   └─ static/                 # CSS, JS, images for frontend
│
└─ README.md

Technologies Used

Frontend:  HTML, CSS, JavaScript

Backend: Python, Flask

Machine Learning: LogisticRegression, scikit-learn , vector tfidf

Chatbot: js based and gemini api key for dynamic chatbot

Database: SQL database for storing candidate data

Libraries: pandas, numpy, joblib, Flask, requests

Installation & Setup
1. Clone the repository
git clone https://github.com/Divya-Gupta17/CareerPath_model
cd CareerPath/backend

2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Run the Flask App
python app.py


Open your browser at http://127.0.0.1:5000/ to view the application.

Dataset

career_data.csv contains:

Candidate skills, interests, academic scores, gender, job status

Recommended careers and course static viewer.

Source: Custom dataset prepared for training the logistic regression

Machine Learning Model

Algorithm: LogisticRegression


Inputs: Skills, interests, education, gender, job status

Outputs: Recommended career paths

Encoders: Label encoders are used to handle categorical variables.

Saved Model: career_model.pkl

Chatbot (SkillBot)

Capabilities:

Answer FAQs about careers and courses

Provide roadmap guidance

Interact conversationally with users

Integration: Embedded in chatbot.html page, communicates with Flask backend via REST API.


Usage

Open the homepage and enter your personal and academic details.

Click Submit to receive recommended career options.

Explore Course Recommendations to enhance your skills.

Interact with the SkillBot Chatbot for guidance and FAQs.

Future Enhancements

Add more ML models to compare recommendation accuracy.

Incorporate real-time data from job portals for better predictions.

Improve chatbot with NLP-based personalized responses.

Add user login and profile management for storing past recommendations.

Authors

Divya Gupta – B.Tech Student | AI & ML Enthusiast
