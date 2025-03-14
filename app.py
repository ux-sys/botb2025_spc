import joblib
import pandas as pd
import random
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for Flash messages & sessions

# File paths
MODEL_FILE = "models/health_ai_model.pkl"
USERS_CSV = "data/patients.csv"

# Load trained AI model
ml_data = joblib.load(MODEL_FILE)
ai_model = ml_data['model']
label_encoders = ml_data['label_encoders']

# Get valid ethnicity and emotion options
valid_ethnicities = list(label_encoders['ethnicity'].classes_)
valid_emotions = list(label_encoders['emotion'].classes_)

def recommend_product(age, height, weight, cholesterol, ethnicity, emotion):
    """Recommends a health product based on user input."""
    bmi = weight / ((height / 100) ** 2)  # Calculate BMI

    if cholesterol > 200:
        return "Heart-Healthy Omega-3 Supplements"
    elif bmi > 25:
        return "Weight Management Program"
    elif emotion.lower() == "stressed":
        return "Mindfulness & Stress Relief App"
    else:
        return "Daily Multivitamins for Overall Health"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            patient_id = random.randint(1000, 9999)
            age = int(request.form['age'])
            height = int(request.form['height'])
            weight = int(request.form['weight'])
            cholesterol = int(request.form['cholesterol'])
            ethnicity = request.form['ethnicity']
            emotion = request.form['emotion']

            # Input validation
            if ethnicity not in valid_ethnicities or emotion not in valid_emotions:
                flash("Invalid ethnicity or emotion. Please select from the dropdown.", "danger")
                return redirect(url_for('register'))

            if age <= 0 or height <= 0 or weight <= 0 or cholesterol < 0:
                flash("Age, height, weight, and cholesterol must be positive numbers!", "danger")
                return redirect(url_for('register'))

            recommended_product = recommend_product(age, height, weight, cholesterol, ethnicity, emotion)

            # Save patient data
            df = pd.read_csv(USERS_CSV) if pd.io.common.file_exists(USERS_CSV) else pd.DataFrame(
                columns=['patient_id', 'age', 'height', 'weight', 'cholesterol', 'ethnicity', 'emotion', 'recommended_product']
            )
            df.loc[len(df)] = [patient_id, age, height, weight, cholesterol, ethnicity, emotion, recommended_product]
            df.to_csv(USERS_CSV, index=False)

            flash(f"Registration successful! Your Patient ID is {patient_id}", "success")
            return render_template('register_success.html', patient_id=patient_id, product=recommended_product)

        except ValueError:
            flash("Invalid input! Please enter valid numbers.", "danger")
            return redirect(url_for('register'))

    return render_template('register.html', ethnicities=valid_ethnicities, emotions=valid_emotions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            patient_id = int(request.form['patient_id'])
            df = pd.read_csv(USERS_CSV)

            if patient_id not in df['patient_id'].values:
                flash("Invalid Patient ID! Please register first.", "danger")
                return redirect(url_for('login'))

            # Store user data in session
            user = df[df['patient_id'] == patient_id].to_dict(orient='records')[0]
            session['user'] = user  # Store user data

            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))

        except ValueError:
            flash("Invalid input! Please enter a valid Patient ID.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash("Please log in first!", "danger")
        return redirect(url_for('login'))
    
    user = session['user']
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
