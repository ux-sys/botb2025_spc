AmbiHealth - AI-Powered Smart Health Recommendations

AmbiHealth is a Flask-based web application that provides personalized health recommendations based on user input, including age, weight, height, cholesterol levels, ethnicity, and emotions. The application uses machine learning to suggest relevant health products tailored to each user's needs.

This is a proof-of-concept (PoC) designed specifically for a competition, meaning it's functional and showcases core ideas but isn’t production-ready. The goal is to demonstrate how AI can leverage user data for smarter health insights.

Technologies & Frameworks Used
AmbiHealth is built using a combination of Python, Flask, and Machine Learning tools:

Python & Flask – Backend framework for handling web requests.
Joblib & Scikit-Learn – Loading and running the AI model.
Pandas – Managing and storing patient data in a CSV file.
Bootstrap 5 – Improving the UI and making it responsive.
Matplotlib – Generating visual health trend charts.
Flask-Session – Handling user authentication and session management.
This project is structured to be easily deployable on Render, Railway, or local environments.

How to Navigate & Interpret the App

1.- Start at the homepage (http://127.0.0.1/)

The homepage introduces the project and allows users to register or log in.
Slogan: “Smarter health, powered by your data.”

2.-Register (http://127.0.0.1/register)

Enter health details like age, weight, height, cholesterol, ethnicity, and emotions to receive a personalized health product recommendation.
The application uses a pre-trained ML model to generate suggestions.

3.- Login (http://127.0.0.1/login)

Use your assigned Patient ID to log in and view your profile.

4.- Dashboard (http://127.0.0.1/dashboard)

Displays stored user data and recommended health product.
Users can see charts showing cholesterol trends over time.

6.- Logout (http://127.0.0.1/logout)

Ends the session and returns to the homepage.
What to check:
AI-Powered Recommendations – Check how the model suggests products based on inputs.
User Experience & Interface – Clean, intuitive, and responsive design.
Functionality & Robustness – Handles errors, validation, and session management properly.
Scalability Potential – Simple CSV-based storage but structured for future database integration.


How to Run Locally
1.- Clone the repository:

git clone https://github.com/ux-sys/otb2025_spc/
cd ./botb2025_spc/AmbiHealth

2.- Install the dependencies:
pip install -r requirements.txt

3.- Run the Flask app:
python app.py

4.- Open in your browser:
http://127.0.0.1:5000/


 Notes & Future Improvements
This is a proof-of-concept, so it currently uses CSV for storage instead of a database.
Future improvements could include SQL database integration, enhanced security, and advanced AI features.
The AI model is pre-trained but could be retrained with more data for better accuracy.

If you run into any issues, restart the Flask server and ensure dependencies are installed correctly.

Feedback & Contributions
Since this is part of a competition, feedback is highly appreciated!
Feel free to leave suggestions or report bugs in the issue tracker.


