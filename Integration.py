import sys
import json
import sklearn.externals as extjoblib
import joblib

def predict_commit_outcome(commit_message, model_path='model.pkl', vectorizer_path='vectorizer.pkl'):
    # Load the model and vectorizer
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    # Feature extraction
    new_commit_vectorized = vectorizer.transform([commit_message])

    # Predict the outcome for the commit
    outcome_prediction = model.predict(new_commit_vectorized)

    # Return the outcome prediction result
    return outcome_prediction[0]

if __name__ == "__main__":
    import sys
    commit_message = sys.argv[1] if len(sys.argv) > 1 else "No Commit Message Found"
    predicted_outcome = predict_commit_outcome(commit_message)
    print(f"{predicted_outcome}")

