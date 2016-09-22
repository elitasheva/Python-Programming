from sales import KEY_TOWN, KEY_PRICE


def find_sales_by_town(dict_sales: list) -> dict:
    towns = {}
    for item in dict_sales:
        town = item[KEY_TOWN]
        price = item[KEY_PRICE]
        towns[town] = towns.get(town, 0) + price
    return towns


def print_sales_by_town(sales_by_town: dict):
    items = sorted(sales_by_town, key=sales_by_town.get, reverse=True)[:5]
    for item in items:
        print(" {}: {:.2f} €".format(item, sales_by_town[item]))
    print()
