from flask import Flask, render_template, request, redirect, url_for
import string
import random

app = Flask(__name__)
url_map = {}  # In-memory storage for URL mappings

def generate_short_code(length=6):
    """Generate a random short code."""
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if short_code not in url_map:
            return short_code

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        url_map[short_code] = long_url
        short_url = request.host_url + short_code
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirects short URL to the original long URL."""
    long_url = url_map.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)