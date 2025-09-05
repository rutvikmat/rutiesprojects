from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# The target URL to scrape
BASE_URL = 'http://quotes.toscrape.com/'


@app.route('/', methods=['GET', 'POST'])
def index():
    jobs = []
    if request.method == 'POST':
        tag = request.form['tag']
        # The site uses 'tags' to filter content, we'll use this to simulate a job search
        search_url = f"{BASE_URL}tag/{tag}/"
        try:
            response = requests.get(search_url)
            response.raise_for_status()  # Raise an exception for bad status codes

            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', class_='quote')

            for quote in quotes:
                # We will treat each 'quote' as a 'job listing' for this example
                title = quote.find('span', class_='text').text
                company = quote.find('small', class_='author').text
                # A link to the author's page can be the 'apply' link
                link = BASE_URL + quote.find('a')['href']

                jobs.append({'title': title, 'company': company, 'link': link})
        except requests.exceptions.RequestException as e:
            jobs = [{'title': f'Error: {e}', 'company': '', 'link': ''}]

    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)