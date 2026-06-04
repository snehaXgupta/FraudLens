import pandas as pd
# Load datasets
fake_df = pd.read_csv("fake_reviews.csv", nrows=500)
amazon_df = pd.read_csv("amazon_reviews.csv", nrows=500)
# FAKE REVIEW DATASET
fake_df = fake_df[['category', 'rating', 'label', 'text_']]
# Convert labels to numeric
fake_df['label'] = fake_df['label'].replace({
    'CG': 1,   # Fake review
    'OR': 0    # Genuine review
})
# Rename columns
fake_df = fake_df.rename(columns={
    'text_': 'review_text'
})
print("Fake Dataset:")
print(fake_df.head())
# AMAZON REVIEW DATASET
amazon_df = amazon_df[['categories', 'reviews.rating', 'reviews.text']]
# Rename columns
amazon_df = amazon_df.rename(columns={
    'categories': 'category',
    'reviews.rating': 'rating',
    'reviews.text': 'review_text'
})
print("\nAmazon Dataset:")
print(amazon_df.head())

# Create labels for amazon reviews
def create_label(rating):
    if rating >= 4:
        return 0   # genuine
    elif rating <= 2:
        return 1   # suspicious/fake
    else:
        return None
amazon_df['label'] = amazon_df['rating'].apply(create_label)
# Remove neutral reviews
amazon_df = amazon_df.dropna(subset=['label'])
print("\nAmazon Dataset with Labels:")
print(amazon_df.head())

# Merge datasets
final_df = pd.concat([fake_df, amazon_df], ignore_index=True)
print("\nFinal Dataset Shape:")
print(final_df.shape)
print("\nFinal Dataset:")
print(final_df.head())
#Cleaning Dataset
# Remove null values
final_df.dropna(inplace=True)
# Remove duplicate reviews
final_df.drop_duplicates(subset=['review_text'], inplace=True)
print("\nDataset After Cleaning:")
print(final_df.shape)
#Text Cleaning
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = text.lower() 
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    return " ".join(words)
# Apply cleaning
final_df['cleaned_review'] = final_df['review_text'].apply(clean_text)
print("\nCleaned Reviews:")

print(final_df[['review_text', 'cleaned_review']].head())
# Save cleaned dataset
final_df.to_csv("final_cleaned_dataset.csv", index=False)