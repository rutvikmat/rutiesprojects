from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)


def generate_password(length=12):
    """Generates a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        # Generate a new password
        password_length = int(request.form.get('length', 12))
        password = generate_password(password_length)

    # Read saved passwords for display
    try:
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        passwords = []

    return render_template('index.html', generated_password=password, saved_passwords=passwords)


@app.route('/save', methods=['POST'])
def save_password():
    """Saves the service and password to a file."""
    service = request.form['service']
    password = request.form['password']
    if service and password:
        with open('passwords.txt', 'a') as f:
            f.write(f"Service: {service}, Password: {password}\n")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)