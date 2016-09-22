from lecture_06.refactor_code.sales import KEY_PRODUCT_ID, KEY_PRICE
from itertools import groupby
from functools import reduce
COLUMN_CATEGORY = -3


def find_sales_by_category(dict_catalog: dict, list_sales: list) -> dict:
    categories = {}
    sorted_catalog = sorted(dict_catalog.values(), key=lambda x: x[COLUMN_CATEGORY])
    grouped_catalog = groupby(sorted_catalog, key=lambda x: x[COLUMN_CATEGORY])
    for key, value in grouped_catalog:
        a = key
        b = list(value)
        d = list(map((lambda x: filter(lambda y: y[KEY_PRODUCT_ID] == x[0], list_sales)), list(value)))
        f = list(filter(lambda y: any(map(lambda x: x[0] == y[KEY_PRODUCT_ID], list(value))), list_sales))
        г = list(filter(lambda y: filter(lambda x: x[0] == y[KEY_PRODUCT_ID], list(value)), list_sales))

        debug = ""
        # {your_key: old_dict[your_key] for your_key in your_keys}




"""categories[key] = reduce((lambda x, y: x + y), )"""

    # for item in list_sales:
    #     item_id = item[KEY_PRODUCT_ID]
    #     price = item[KEY_PRICE]
    #     category = dict_catalog[item_id][COLUMN_CATEGORY]
    #     categories[category] = categories.get(category, 0) + price
    #
    # return categories


def print_sales_by_category(sales_by_category: dict):
    items = sorted(sales_by_category, key=sales_by_category.get, reverse=True)[:5]
    for item in items:
        print(" {}: {:.2f} €".format(item, sales_by_category[item]))
    print()

