# utils.py
import requests

def validate_currency_code(currency_code):
    api_url = 'https://api.exchangerate.host/symbols'
    response = requests.get(api_url)
    currencies = response.json().get('symbols', {})

    return currency_code in currencies

def convert_currency(from_currency, to_currency, amount):
    api_url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        if 'result' in data:
            converted_amount = data['result']
            return f"{get_currency_symbol(to_currency)} {converted_amount:.2f}"
        else:
            return f"Error: {data.get('error', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def validate_input(from_currency, to_currency, amount):
    if not validate_currency_code(from_currency) or not validate_currency

    def validate_input(from_currency, to_currency, amount):
    if not validate_currency_code(from_currency) or not validate_currency_code(to_currency):
        return "Invalid currency code. Please enter a valid three-letter currency code."

    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount. Please enter a valid number."

    return None

def get_currency_symbol(currency_code):
    # You can implement this function to return the currency symbol based on the currency code.
    # For simplicity, let's return the currency code as a symbol.
    return currency_code
