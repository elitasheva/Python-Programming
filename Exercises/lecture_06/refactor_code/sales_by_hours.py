from lecture_06.refactor_code.sales import KEY_TIME, KEY_PRICE
from itertools import groupby
from functools import reduce


def find_sales_by_hours(list_sales: list) -> dict:
    hours = {}
    list_sales.sort(key=lambda x: x[KEY_TIME].replace(minute=0, second=0, microsecond=0))
    grouped_data = groupby(list_sales, key=lambda x: x[KEY_TIME].replace(minute=0, second=0, microsecond=0))
    for key, value in grouped_data:
        hours[key] = reduce((lambda x, y: x + y), list(map((lambda x: x[KEY_PRICE]), list(value))))
    return hours


def print_sales_by_hours(sales_by_hours: dict):
    items = sorted(sales_by_hours, key=sales_by_hours.get, reverse=True)[:5]
    for item in items:
        print(" {}: {:.2f} €".format(item, sales_by_hours[item]))
    print()

