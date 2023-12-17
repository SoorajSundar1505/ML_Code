import joblib

model_path = '/content/model.pkl'
vectorizer_path = '/content/vectorizer.pkl'
joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)