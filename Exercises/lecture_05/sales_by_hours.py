from sales import KEY_TIME, KEY_PRICE


def find_sales_by_hours(dict_sales: list)-> dict:
    hours = {}
    for item in dict_sales:
        time = item[KEY_TIME].replace(minute=0, second=0, microsecond=0)
        price = item[KEY_PRICE]
        hours[time] = hours.get(time, 0) + price
    return hours


def print_sales_by_hours(sales_by_hours: dict):
    items = sorted(sales_by_hours, key=sales_by_hours.get, reverse=True)[:5]
    for item in items:
        print(" {}: {:.2f} €".format(item, sales_by_hours[item]))
    print()
