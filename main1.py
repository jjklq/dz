import currency_converter

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.72
}

def convert(amount, from_currency, to_currency):
    """
    Преобразует сумму из одной валюты в другую с использованием обменных курсов.

    :param amount: Сумма для конвертации.
    :param from_currency: Исходная валюта.
    :param to_currency: Целевая валюта.
    :return: Сумма в целевой валюте.
    """
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Неизвестная валюта")

  
    converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
    return converted_amount
