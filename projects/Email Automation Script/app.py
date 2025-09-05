from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# --- CONFIGURATION ---
# IMPORTANT: Replace with your own email credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_app_password'  # Use an App Password for Gmail


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']

        try:
            # Create the email
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient

            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, [recipient], msg.as_string())
            message = "Email sent successfully!"
        except Exception as e:
            message = f"Failed to send email: {e}"

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)