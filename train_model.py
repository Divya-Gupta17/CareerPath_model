# train_model.py

import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv("recommendation.csv")

# Normalize and combine features
def normalize_text(row):
    text = f"{row['Education']} {row['Skills']} {row['Interests']}".lower()
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

df["combined"] = df.apply(normalize_text, axis=1)

# Prepare data
X = df["combined"]
y = df["Recommended_Career"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(pipeline, "model.joblib")
print("✅ Model saved to model.joblib")
