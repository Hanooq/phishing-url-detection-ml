"""
Educational phishing URL classification demo.
IMPORTANT: This project uses a SIMULATED dataset, not verified real URLs.
It demonstrates a basic ML workflow and must not be used as a real security product.
"""
from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA = Path(__file__).with_name("simulated_phishing_url_dataset.csv")
MODEL = Path(__file__).with_name("phishing_url_model.joblib")

def main():
    data = pd.read_csv(DATA)
    X = data.drop(columns=["label"])
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    model = RandomForestClassifier(
        n_estimators=120, max_depth=8, random_state=42, class_weight="balanced"
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Rows: {len(data)} | Training: {len(X_train)} | Testing: {len(X_test)}")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print("\\nClassification report:")
    print(classification_report(y_test, predictions, target_names=["Legitimate", "Phishing"]))
    print("Confusion matrix (rows=true, columns=predicted):")
    print(confusion_matrix(y_test, predictions))
    print("\\nFeature importance:")
    print(pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False))
    joblib.dump(model, MODEL)
    print(f"\\nSaved model to: {MODEL.name}")

if __name__ == "__main__":
    main()
