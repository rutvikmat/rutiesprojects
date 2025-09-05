from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key. In a real app, you would save and reuse this key.
# For this example, we'll use a fixed key for simplicity.
# To generate a new key: key = Fernet.generate_key()
# For demonstration, we use a static key. Keep this key safe!
key = b'pLdZtY9zJ2b5n8x/A?D(G+KbPeShVmYq'  # Example Key, must be 32 url-safe base64-encoded bytes
cipher_suite = Fernet(key)


@app.route('/', methods=['GET', 'POST'])
def index():
    processed_text = ""
    original_text = ""
    if request.method == 'POST':
        text = request.form['text']
        original_text = text
        action = request.form['action']

        if action == 'encrypt':
            encrypted_text = cipher_suite.encrypt(text.encode())
            processed_text = encrypted_text.decode()
        elif action == 'decrypt':
            try:
                decrypted_text = cipher_suite.decrypt(text.encode())
                processed_text = decrypted_text.decode()
            except Exception:
                processed_text = "Decryption Failed: Invalid key or corrupt data."

    return render_template('index.html', processed_text=processed_text, original_text=original_text)


if __name__ == '__main__':
    app.run(debug=True)