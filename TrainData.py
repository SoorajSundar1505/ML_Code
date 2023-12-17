import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read the dataset
dataset_path = '/content/DataSet.csv'  # Replace with the actual path to your dataset
dataset = pd.read_csv(dataset_path)

# Preprocess the data (optional, depending on your dataset)
dataset['CommitMessage'] = dataset['CommitMessage'].str.lower()

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    dataset['CommitMessage'], dataset['Outcome'], test_size=0.2, random_state=42
)

# Vectorize the text data
vectorizer = TfidfVectorizer()
train_vectorized = vectorizer.fit_transform(train_data)
test_vectorized = vectorizer.transform(test_data)

# Train the model
model = LogisticRegression()
model.fit(train_vectorized, train_labels)

# Make predictions on the test set
predictions = model.predict(test_vectorized)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
print(f"Model Accuracy: {accuracy}")