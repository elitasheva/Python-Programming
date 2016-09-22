import sqlite3
import csv
from lecture_07_01.load_data import load_catalog, load_sales
FILE_NAME = "data.db"
CATALOG_PATH = "./resources/catalog.csv"
SALES_PATH = "./resources/sales-10K.csv"
COLUMN_PRODUCT_ID = 0
COLUMN_COUNTRY = 1
COLUMN_TOWN = 2
COLUMN_TIME = 3
COLUMN_PRICE = 4

KEY_PRODUCT_ID = "product_id"
KEY_COUNTRY = "country"
KEY_TOWN = "town"
KEY_TIME = "time"
KEY_PRICE = "price"

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5


def main():
    input_city = input("Въведете име на град: ")
    with sqlite3.connect(FILE_NAME, isolation_level=None) as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='sale'""")
        table_exists = cursor.fetchall()

        if not any(table_exists):
            create_tables(connection)
            fill_catalog_table(connection, CATALOG_PATH)
            print("Catalog loaded")
            fill_sale_table(connection, SALES_PATH)
            print("Sales loaded")

        cursor.execute("""SELECT item_key,sale_timestamp,price FROM sale WHERE city_name = ? order by sale_timestamp desc""", [input_city])
        result = cursor.fetchall()
        if not any(result):
            print("Няма данни за продажби в град {}".format(input_city))
        else:
            for item_key, timestamp, price in result:
                print("Артикул  #: {}   дата/час: {}   сума: {:.2f}".format(item_key, timestamp, price))


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""create table if not exists sale (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_key varchar(200) NOT NULL,
                        country varchar(3),
                        city_name varchar(60),
                        sale_timestamp TEXT,
                        price NUMERIC); """)

    cursor.execute("""create table if not exists catalog (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_key varchar(200),
                    category varchar(200));""")


def fill_catalog_table(connection, path):
    cursor = connection.cursor()
    # with open(path, encoding="utf-8") as csv_file:
    #     reader = csv.reader(csv_file)
    #     for row in reader:
    #         item_key = row[COLUMN_PRODUCT_ID]
    #         category = row[COLUMN_CATEGORY]
    #         cursor.execute("""insert into catalog (item_key, category) values (?,?)""", [item_key, category])
    #         print(row)
    catalog = load_catalog(path)
    for item_key, category in catalog.items():
        cursor.execute("""insert into catalog (item_key, category) values (?,?)""", [item_key, category])
        print(item_key)


def fill_sale_table(connection, path):
    cursor = connection.cursor()
    # with open(path, encoding="utf-8") as csv_file:
    #     reader = csv.reader(csv_file)
    #     for row in reader:
    #         item_key = row[COLUMN_PRODUCT_ID]
    #         country = row[COLUMN_COUNTRY]
    #         city_name = row[COLUMN_TIME]
    #         sale_timestamp = row[COLUMN_TIME]
    #         price = float(row[COLUMN_PRICE])
    #         cursor.execute("""insert into sale (item_key, country, city_name, sale_timestamp, price)
    #                         values (?, ?, ? , ?, ?)""", [item_key, country, city_name, sale_timestamp, price])
    #         print(row)
    sales = load_sales(path)
    for sale in sales:
        item_key = sale[KEY_PRODUCT_ID]
        country = sale[KEY_COUNTRY]
        city_name = sale[KEY_TOWN]
        sale_timestamp = sale[KEY_TIME].isoformat()
        price = float(sale[KEY_PRICE])
        cursor.execute("""insert into sale (item_key, country, city_name, sale_timestamp, price)
                        values (?, ?, ? , ?, ?)""", [item_key, country, city_name, sale_timestamp, price])
        print(item_key)


if __name__ == '__main__':
    main()
