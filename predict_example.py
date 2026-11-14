from pathlib import Path
import joblib
import pandas as pd

MODEL = Path(__file__).with_name("phishing_url_model.joblib")

def predict_example():
    if not MODEL.exists():
        raise SystemExit("Model not found. Run train_model.py first.")
    model = joblib.load(MODEL)
    example = pd.DataFrame([{
        "url_length": 72,
        "num_dots": 4,
        "num_hyphens": 3,
        "has_at_symbol": 1,
        "uses_ip_address": 0,
        "uses_https": 0,
        "num_digits": 8,
        "suspicious_word_count": 2,
        "uses_url_shortener": 0
    }])
    prediction = int(model.predict(example)[0])
    print("Prediction:", "Potentially phishing" if prediction == 1 else "Likely legitimate")
    print("This is only an educational demonstration using simulated training data.")

if __name__ == "__main__":
    predict_example()
