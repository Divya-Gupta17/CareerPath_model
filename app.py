from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for
import joblib
import numpy as np
import mysql.connector 
import os
import re

app = Flask(__name__)

# Load model and encoders
app.secret_key = os.urandom(24)

# Database connection
conn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="career_ap"
)
cursor = conn.cursor()

# Dummy career-course mappings
career_courses = {
    "Data Scientist": ["Python for Data Science", "Machine Learning A-Z", "Deep Learning Specialization"],
    "Software Engineer": ["C++ DSA Masterclass", "System Design Basics", "Clean Code by Uncle Bob"],
    "UI/UX Designer": ["Adobe XD Masterclass", "Figma UI/UX Design", "User Psychology 101"]
}

# Load your ML model
model = joblib.load("model.joblib")

# Preprocessing input
def normalize_input(education, skills, interests):
    text = f"{education} {skills} {interests}".lower()
    replacements = {
        "ai": "artificial intelligence",
        "ml": "machine learning",
        "web dev": "web development",
        "app dev": "mobile development",
        "js": "javascript",
        "reactjs": "react",
        "nodejs": "node",
        "data analysis": "data analytics"
    }
    for key, val in replacements.items():
        text = re.sub(rf"\b{re.escape(key)}\b", val, text)
    return text

# Routes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("SELECT * FROM `user` WHERE `email` = %s AND `password` = %s", (email, password))
    users = cursor.fetchall()

    if len(users) > 0:
        session['user_id'] = users[0][0]
        session['firstname'] = users[0][1]  # Assuming the first name is stored at index 1
        print(f"User ID: {session['user_id']}, Firstname: {session['firstname']}")  # Debugging session values
        return redirect(url_for('user_dashboard'))
    else:
        flash('Invalid Email or Password', 'danger')
        return redirect(url_for('login'))

@app.route('/add_user', methods=['POST'])
def add_user():
    firstname = request.form.get('ufirstName')
    lastname = request.form.get('ulastName')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    sql = "INSERT INTO `user` (`id`, `firstname`, `lastname`, `email`, `password`) VALUES (NULL, %s, %s, %s, %s)"
    values = (firstname, lastname, email, password)

    try:
        cursor.execute(sql, values)
        conn.commit()
        flash('Registration Successful! Please login.', 'success')
        return redirect(url_for('login'))
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        flash('Registration failed. Try again.', 'danger')
        return redirect(url_for('register'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if name and email and message:
            flash("Your message has been sent successfully!", "success")
        else:
            flash("Please fill in all required fields.", "warning")

        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    prediction = None
    name = None
    if request.method == "POST":
        name = request.form.get("name")
        education = request.form.get("education")
        skills = request.form.get("skills")
        interests = request.form.get("interests")

        combined_text = normalize_input(education, skills, interests)
        prediction = model.predict([combined_text])[0]

    return render_template("recommend.html", prediction=prediction, name=name)

@app.route('/career', methods=['GET', 'POST'])
def career():
    if request.method == 'POST':
        education = request.form.get("education")
        skills = request.form.get("skills").split(",")
        interests = request.form.get("interests").split(",")

        try:
            # Assuming you have label_encoders
            edu_encoded = label_encoder.transform([education])[0]
            skills_encoded = skills_encoder.transform([skills])
            interests_encoded = interests_encoder.transform([interests])

            input_features = np.concatenate(([[edu_encoded]], skills_encoded, interests_encoded), axis=1)
            prediction = model.predict(input_features)
            predicted_career = label_encoder.inverse_transform(prediction)[0]

            return render_template("career.html", prediction=predicted_career)
        except Exception as e:
            return render_template("career.html", error=str(e))
    return render_template("career.html", prediction=None)

@app.route('/courses')
def courses():
    career = request.args.get("career")
    courses_list = career_courses.get(career, ["Coming Soon"])
    return render_template("courses.html", career=career, courses=courses_list)


@app.route('/ai_chatbot')
def ai_chatbot():
    return render_template('ai_chatbot.html')

@app.route('/chatbot')
def chatbot_page():
    return render_template('chatbot.html')
def get_trendy_job_searches():
    trendy_labels = [
        "Data Scientist", 
        "Web Developer", 
        "AI Engineer", 
        "Software Engineer",
        "UX/UI Designer",
        "Cloud Architect",
        "DevOps Engineer",
        "Product Manager"
    ]
    trendy_values = [35, 42, 27, 15, 32, 24, 18, 29]
    return trendy_labels, trendy_values

def get_overall_market_trends():
    market_labels = [
        "Tech", 
        "Finance", 
        "Healthcare", 
        "Education", 
        "Retail", 
        "Manufacturing", 
        "Energy", 
        "Government"
    ]
    market_values = [58, 38, 42, 25, 18, 21, 33, 20]
    return market_labels, market_values

@app.route('/user_dashboard')
def user_dashboard():
    if 'user_id' in session:
        firstname = session.get('firstname', 'User')  # Default to 'User' if not found
        print(f"User Dashboard - Firstname: {firstname}")  # Debugging session value
               
        

 

    # Job search links
        job_search_links =job_search_links = {
    "LinkedIn": {
        "url": "https://www.linkedin.com/jobs",
        "description": "A professional networking platform where companies of all sizes post job openings. Known for its robust search filters and networking capabilities."
    },
    "Indeed": {
        "url": "https://www.indeed.com",
        "description": "One of the largest job search engines, aggregating listings from various company websites and job boards. Offers a wide range of job types and locations."
    },
    "Glassdoor": {
        "url": "https://www.glassdoor.com/Job/index.htm",
        "description": "In addition to job listings, Glassdoor provides company reviews, salary information, and insights into company culture, helping you make informed decisions."
    },
    "AngelList": {
        "url": "https://angel.co/jobs",
        "description": "A platform primarily focused on startups and early-stage companies. Ideal for those looking for roles in innovative and fast-growing environments."
    }
}
        # Articles on the latest tech trends
        tech_articles =[
  {
    "title": "AI and the Future of Work: Insights from the World Economic Forum's Future of Jobs Report 2025",
    "link": "https://www.sandtech.com/insight/ai-and-the-future-of-work/"
  },
  {
    "title": "2025 will see huge advances in quantum computing. So what is a quantum chip and how does it work?",
    "link": "https://www.csiro.au/en/news/All/Articles/2025/January/2025-huge-advances-in-quantum-computing"
  },
  {
    "title": "Blockchain Beyond Cryptocurrency: Real-World Applications Transforming Industries",
    "link": "https://www.entrepreneur.com/en-in/news-and-trends/blockchain-beyond-cryptocurrency-real-world-applications/489297"
  }
]
        # Get trendy job searches and market trends
        trendy_labels, trendy_values = get_trendy_job_searches()
        market_labels, market_values = get_overall_market_trends()
        
        # Zip the lists in Python before passing them to the template
        trendy_data = list(zip(trendy_labels, trendy_values))
        market_data = list(zip(market_labels, market_values))
        

       
        return render_template(
            'user_dashboard.html',
            firstname=firstname,
            trendy_data=trendy_data,
            market_data=market_data,
            job_search_links=job_search_links,
            tech_articles=tech_articles
        )
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5004)