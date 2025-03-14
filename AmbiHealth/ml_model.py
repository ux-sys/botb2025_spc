import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

DATA_FILE = "data/health_data.csv"
MODEL_FILE = "models/health_ai_model.pkl"

def train_model():
    # Load dataset
    df = pd.read_csv(DATA_FILE)

    # Encode categorical features
    label_encoders = {}
    for col in ['ethnicity', 'emotion', 'recommended_product']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Split data
    X = df[['age', 'height', 'weight', 'cholesterol', 'ethnicity', 'emotion']]
    y = df['recommended_product']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model and encoders
    joblib.dump({'model': model, 'label_encoders': label_encoders}, MODEL_FILE)

    print("✅ AI Model Trained & Saved!")

if __name__ == "__main__":
    train_model()
