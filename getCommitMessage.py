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

  if outcome_prediction[0] == 1:
        # Define your keywords
        keywords = ['keyword1', 'keyword2', 'keyword3']  # Replace with your actual keywords

        # Check if any keyword is present in the commit message
        matched_keywords = [kw for kw in keywords if kw in commit_message.lower()]

        # If any keyword is matched, save the commit message and matched keyword(s) to a file
        if matched_keywords:
            with open("output.txt", "w") as f:
                print(f"Commit Message: {commit_message}", file=f)
                print("Matched Keywords:", file=f)
                for matched_keyword in matched_keywords:
                    print(matched_keyword, file=f)
            return matched_keywords
        else:
            print("No matching keywords found in the commit message.")
            return None  # or return some default value
    else:
        print("Prediction outcome is not 1. Skipping keyword check.")
        return None  # or return some default value

if __name__ == "__main__":
    import sys

    commit_message = sys.argv[1] if len(sys.argv) > 1 else "No Commit Message Found"
    print(f"Received commit message: {commit_message}")

    # Call the function and get the matched keywords
    matched_keywords = predict_commit_outcome(commit_message)

    if matched_keywords is not None:
        print(f"Matched Keywords are: {matched_keywords}")

    print("Prediction process completed.")
