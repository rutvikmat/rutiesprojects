from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained vectorizer and classifier
vectorizer = joblib.load('spam_vectorizer.pkl')
classifier = joblib.load('spam_classifier.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    email_text = ""
    if request.method == 'POST':
        email_text = request.form['email_text']
        if email_text:
            # Vectorize the input text
            email_counts = vectorizer.transform([email_text])
            # Make a prediction
            pred = classifier.predict(email_counts)
            prediction = pred[0].upper()

    return render_template('index.html', prediction=prediction, email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)