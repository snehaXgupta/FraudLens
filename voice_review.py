import speech_recognition as sr
import joblib
import re
import nltk
from nltk.corpus import stopwords
# DOWNLOAD STOPWORDS
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
# LOAD MODEL AND VECTORIZER

model = joblib.load("fake_review_model.pkl")

vectorizer = joblib.load("tfidf_vectorizer.pkl")

# TEXT CLEANING FUNCTION
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Speech Recognition
recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("\nSpeak your review now...")

    recognizer.adjust_for_ambient_noise(source)

    audio = recognizer.listen(source)

    print("\nProcessing speech...")

# CONVERT SPEECH TO TEXT
try:

    review = recognizer.recognize_google(audio)
    print("\nRecognized Review:")
    print(review)

    # CLEAN TEXT
    cleaned_review = clean_text(review)
    # VECTORIZE
    review_vector = vectorizer.transform([cleaned_review])
    # PREDICT
    prediction = model.predict(review_vector)
    
    # OUTPUT
    if prediction[0] == 1:
        print("\nFake Review Detected")
    else:
        print("\nGenuine Review")

# error handling

except sr.UnknownValueError:

    print("\nCould not understand audio")

except sr.RequestError:

    print("\nInternet connection error")