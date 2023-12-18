import sys
import json
import requests
import joblib
import os

session = requests.Session()
session.verify = False

# Load the trained model and vectorizer
model_path = 'model.pkl'
vectorizer_path = 'vectorizer.pkl'

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Provide a new commit message for testing
commit_message = os.environ.get('CHANGE_MESSAGE', '')

# Feature extraction
new_commit_vectorized = vectorizer.transform([commit_message])

# Predict the outcome for the commit
outcome_prediction = model.predict(new_commit_vectorized)

# Print the outcome prediction result
print(f"Predicted Outcome: {outcome_prediction[0]}")

#Return the predicted outcome
sys.exit(outcome_prediction[0])


