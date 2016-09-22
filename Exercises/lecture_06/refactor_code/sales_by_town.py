from lecture_06.refactor_code.sales import KEY_TOWN, KEY_PRICE
from itertools import groupby
from functools import reduce


def print_sales_by_town(sales_by_town: dict):
    items = sorted(sales_by_town, key=sales_by_town.get, reverse=True)[:5]
    for item in items:
        print(" {}: {:.2f} €".format(item, sales_by_town[item]))
    print()


def print_neshtosi(key, value):
    print(" {}: {:.2f} €".format(key, value))


def find_sales_by_town(list_sales: list) -> dict:
    towns = {}
    list_sales.sort(key=lambda x: x[KEY_TOWN])
    grouped_data = groupby(list_sales, key=lambda x: x[KEY_TOWN])
    for key, value in grouped_data:
        towns[key] = reduce((lambda x, y: x + y), list(map((lambda x: x[KEY_PRICE]), list(value))))
    items = sorted(towns, key=towns.get, reverse=True)[:5]
    list(map((lambda x: print_neshtosi(x, towns[x])), items))
    return towns



