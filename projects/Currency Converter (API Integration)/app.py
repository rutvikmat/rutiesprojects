from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual key from exchangerate-api.com
API_KEY = 'YOUR_API_KEY'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

# A list of common currencies for the dropdown
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'INR', 'CNY']


@app.route('/', methods=['GET', 'POST'])
def index():
    converted_result = None
    error = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        try:
            # Fetch the exchange rates
            response = requests.get(BASE_URL + from_currency)
            data = response.json()

            if data['result'] == 'success':
                exchange_rate = data['conversion_rates'][to_currency]
                converted_amount = round(amount * exchange_rate, 2)
                converted_result = f"{amount} {from_currency} = {converted_amount} {to_currency}"
            else:
                error = "Could not retrieve exchange rates."
        except Exception as e:
            error = f"An error occurred: {e}"

    return render_template('index.html', currencies=currencies, result=converted_result, error=error)


if __name__ == '__main__':
    app.run(debug=True)