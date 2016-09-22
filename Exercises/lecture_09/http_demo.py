import requests
from urllib.parse import urljoin
import iso8601
import sys
from decimal import Decimal
API_URL = "http://api.fixer.io/"

user_input_date_str = input("Въведете дата във формат година-месец-ден: ")
user_input_currency = input("Въведете валута: ")
user_input_amount_str = input("Въведете сума: ")
user_target_currency = input("Въведете валута, към която да се конвертира: ")
user_input_currency = user_input_currency.upper()
user_target_currency = user_target_currency.upper()

date_str = None
try:
    date_obj = iso8601.parse_date(user_input_date_str)
    date_str = date_obj.strftime("%Y-%m-%d")
except iso8601.iso8601.ParseError:
    print("Невалидна дата!")
    sys.exit()

new_url_str = urljoin(API_URL, date_str)

print("Извличане на валути...")
response = requests.get(new_url_str, timeout=20, params={'base': user_target_currency})
if response.status_code == 200:
    response_json_dict = response.json()

    rates = response_json_dict.get('rates', {})
    exchange_rate = rates.get(user_input_currency, None)
    if not exchange_rate:
        print("Няма информация за въведената валута.")
    else:
        user_input_amount_decimal = Decimal(user_input_amount_str)
        exchange_rate_decimal = Decimal(exchange_rate)
        result = user_input_amount_decimal / exchange_rate_decimal
        print("Равностойност в {}: {:.2f}".format(user_target_currency, result))
else:
    print("Грешка при сървъра!", response.status_code)
