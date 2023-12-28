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
    # return str(outcome_prediction[0])
    # Redirect the standard output to a file

  if outcome_prediction[0]==1:
    keywords = ['login', 'home']  # Replace with your actual keywords

        # Check if any keyword is present in the commit message
        matched_keywords = [kw for kw in keywords if kw in commit_message.lower()]

        # If any keyword is matched, save the matched keyword to a file
        if matched_keywords:
            with open("output.txt", "w") as f:
                for matched_keyword in matched_keywords:
                    print(matched_keyword, file=f)
        else:
            print("No matching keywords found in the commit message.")
    else:
        print("Prediction outcome is not 1. Skipping keyword check.")
    
    with open("output.txt", "w") as f:
        print(outcome_prediction[0], file=f)

    # Exit with a success code
    sys.exit(0)


if __name__ == "__main__":
    import sys
    commit_message = sys.argv[1] if len(sys.argv) > 1 else "No Commit Message Found"
    print(f"Received commit message: {sys.argv[1]}")
    predicted_outcome = predict_commit_outcome(commit_message)
    print(f"Received Outcome is: {predicted_outcome}")
