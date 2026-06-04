import pandas as pd
# Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# Save model
import joblib
# Load Cleaned Dataset
df = pd.read_csv("final_cleaned_dataset.csv")
# Remove empty reviews
df.dropna(subset=['cleaned_review'], inplace=True)
# INPUT AND OUTPUT
X = df['cleaned_review']
y = df['label']

# TF-IDF VECTORIZATION
vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)
# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# LOGISTIC REGRESSION
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
# PREDICTION
lr_pred = lr_model.predict(X_test)
# EVALUATION
lr_accuracy = accuracy_score(y_test, lr_pred)
print(f"\n Logistic Regression Accuracy: {lr_accuracy * 100:.2f}%")
print("\n Logistic Regression Classification Report:\n")
print(classification_report(y_test, lr_pred))


# NAIVE BAYES MODEL
from sklearn.naive_bayes import MultinomialNB
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
# Predictions
nb_pred = nb_model.predict(X_test)
#Accuracy
nb_accuracy = accuracy_score(y_test, nb_pred)
print(f"\nNaive Bayes Accuracy: {nb_accuracy * 100:.2f}%")
print("\nNaive Bayes Classification Report:\n")
print(classification_report(y_test, nb_pred))

# RANDOM FOREST MODEL
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)
# Predictions
rf_pred = rf_model.predict(X_test)
# Accuracy
rf_accuracy = accuracy_score(y_test, rf_pred)
print(f"\nRandom Forest Accuracy: {rf_accuracy * 100:.2f}%")
print("\nRandom Forest Classification Report:\n")
print(classification_report(y_test, rf_pred))

#Save the Best Model 
joblib.dump(lr_model, "fake_review_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")