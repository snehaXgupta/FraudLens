import joblib
import re
import nltk
from nltk.corpus import stopwords
# Download stopwords
nltk.download('stopwords')
# Load stopwords
stop_words = set(stopwords.words('english'))
# LOAD SAVED MODEL AND VECTORIZER
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
print("Model Loaded Successfully!")
# TEXT CLEANING FUNCTION
def clean_text(text):
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)
# USER INPUT
review = input("\nEnter Product Review:\n")
# Clean review
cleaned_review = clean_text(review)
# Convert to vector
review_vector = vectorizer.transform([cleaned_review])
# Prediction
prediction = model.predict(review_vector)

# OUTPUT

if prediction[0] == 1:
    print("\nFake Review Detected")
else:
    print("\nGenuine Review")