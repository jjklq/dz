# plotter.py

import matplotlib.pyplot as plt

years = list (range(2000, 2023))
exchange_rates = [
    5.64, 5.61, 5.12, 5.05, 5.07, 5.08, 5.05, 4.48, 4.21, 4.00, 3.84, 3.14, 2.79, 2.39,
    2.34, 1.99, 1.87, 1.89, 1.80, 1.86, 2.30, 2.70, 2.75
]

plt.figure(figsize=(10, 6))
plt.plot(years, exchange_rates, marker='o', linestyle='-')
plt.title("UAH/USD Exchange Rate (2000-2022)")
plt.xlabel("Year")
plt.ylabel("Exchange Rate (UAH to USD)")
plt.grid(True)
plt.show()


# currency_converter.py

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 110.47,
    "AUD": 1.35,
    "CAD": 1.27,
    "CHF": 0.92,
    "CNY": 6.46,
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Invalid currency codes."

if __name__ == "__main__":
    amount = 100
    from_currency = "USD"
    to_currency = "EUR"
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")
