import requests
from bs4 import BeautifulSoup

import joblib
import re
import nltk

from nltk.corpus import stopwords

# ---------------------------------------
# DOWNLOAD STOPWORDS
# ---------------------------------------

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# ---------------------------------------
# LOAD MODEL + VECTORIZER
# ---------------------------------------

model = joblib.load("fake_review_model.pkl")

vectorizer = joblib.load("tfidf_vectorizer.pkl")

print("Model Loaded Successfully!")

# ---------------------------------------
# TEXT CLEANING FUNCTION
# ---------------------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# ---------------------------------------
# USER INPUT LINK
# ---------------------------------------

url = input("\nEnter Product URL:\n")

# ---------------------------------------
# HEADERS
# ---------------------------------------

headers = {
    "User-Agent":
    "Mozilla/5.0"
}

# ---------------------------------------
# SEND REQUEST
# ---------------------------------------

response = requests.get(url, headers=headers)

# ---------------------------------------
# PARSE HTML
# ---------------------------------------

soup = BeautifulSoup(response.text, "html.parser")

# ---------------------------------------
# FIND REVIEWS
# ---------------------------------------

reviews = soup.find_all("div", class_="_6K-7Co")

# ---------------------------------------
# CHECK REVIEWS
# ---------------------------------------

if not reviews:

    print("\nNo reviews found!")

else:

    print(f"\nFound {len(reviews)} reviews\n")

# ---------------------------------------
# ANALYZE REVIEWS
# ---------------------------------------

for i, review in enumerate(reviews[:10]):

    review_text = review.get_text(strip=True)

    print(f"\nReview {i+1}:")
    print(review_text)

    # ---------------------------------------
    # CLEAN TEXT
    # ---------------------------------------

    cleaned_review = clean_text(review_text)

    # ---------------------------------------
    # VECTORIZE
    # ---------------------------------------

    review_vector = vectorizer.transform([cleaned_review])

    # ---------------------------------------
    # PREDICT
    # ---------------------------------------

    prediction = model.predict(review_vector)

    # ---------------------------------------
    # OUTPUT
    # ---------------------------------------

    if prediction[0] == 1:
        result = "Fake Review"
    else:
        result = "Genuine Review"

    print("Prediction:", result)