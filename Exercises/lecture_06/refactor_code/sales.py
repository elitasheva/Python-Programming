import csv
import iso8601

KEY_PRODUCT_ID = "product_id"
KEY_COUNTRY = "country"
KEY_TOWN = "town"
KEY_TIME = "time"
KEY_PRICE = "price"

COLUMN_PRODUCT_ID = 0
COLUMN_COUNTRY = 1
COLUMN_TOWN = 2
COLUMN_TIME = 3
COLUMN_PRICE = 4


def load_sales(filename: str) -> list:
    sales = []
    with open(filename, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            current_sale = {KEY_PRODUCT_ID: line[COLUMN_PRODUCT_ID],
                            KEY_COUNTRY: line[COLUMN_COUNTRY],
                            KEY_TOWN: line[COLUMN_TOWN],
                            KEY_TIME: iso8601.parse_date(line[COLUMN_TIME]),
                            KEY_PRICE: float(line[COLUMN_PRICE])}
            sales.append(current_sale)
        return sales

