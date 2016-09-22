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

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5


def load_sales(filename: str) -> list:

    with open(filename, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            current_sale = {KEY_PRODUCT_ID: line[COLUMN_PRODUCT_ID],
                            KEY_COUNTRY: line[COLUMN_COUNTRY],
                            KEY_TOWN: line[COLUMN_TOWN],
                            KEY_TIME: iso8601.parse_date(line[COLUMN_TIME]),
                            KEY_PRICE: float(line[COLUMN_PRICE])}
            yield current_sale


def load_catalog(filename: str) -> dict:
    catalog_by_id = {}
    with open(filename, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            product_id = line[COLUMN_PRODUCT_ID]
            category = line[COLUMN_CATEGORY]
            catalog_by_id[product_id] = category
    return catalog_by_id
