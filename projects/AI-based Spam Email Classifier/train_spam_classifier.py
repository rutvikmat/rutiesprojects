import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the dataset
df = pd.read_csv('spam_data.csv')

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into a matrix of token counts
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Test the model
X_test_counts = vectorizer.transform(X_test)
accuracy = clf.score(X_test_counts, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the vectorizer and the model
joblib.dump(vectorizer, 'spam_vectorizer.pkl')
joblib.dump(clf, 'spam_classifier.pkl')

print("Vectorizer and model saved successfully!")