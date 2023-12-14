# app.py
from flask import Flask, render_template, request
from utils import validate_currency_code, convert_currency

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = request.form['amount']

        # Validate currency codes and amount
        error_message = validate_input(from_currency, to_currency, amount)

        if error_message:
            return render_template('index.html', error_message=error_message)

        # Convert currency
        result = convert_currency(from_currency, to_currency, amount)
        return render_template('index.html', result=result)

    return render_template('index.html')

def validate_input(from_currency, to_currency, amount):
    if not validate_currency_code(from_currency) or not validate_currency_code(to_currency):
        return "Invalid currency code. Please enter a valid three-letter currency code."

    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount. Please enter a valid number."

    return None

if __name__ == '__main__':
    app.run(debug=True)
# utils.py
import requests

def validate_currency_code(currency_code):
    # this function based on the API response for currency code validation
    # assume that the API returns a list of supported currencies
    api_url = 'https://api.exchangerate.host/symbols'
    response = requests.get(api_url)
    currencies = response.json().get('symbols', {})

    return currency_code in currencies

def convert_currency(from_currency, to_currency, amount):
    api_url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}'
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        converted_amount = data.get('result', 0)
        return f"{to_currency} {converted_amount:.2f}"

    return f"Error: {data.get('error', 'Unknown error')}"

