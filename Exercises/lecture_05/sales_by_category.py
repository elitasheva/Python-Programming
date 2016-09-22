from sales import KEY_PRODUCT_ID, KEY_PRICE
COLUMN_CATEGORY = 5


def find_sales_by_category(dict_catalog: dict, dict_sales: list) -> dict:
    categories = {}
    for item in dict_sales:
        item_id = item[KEY_PRODUCT_ID]
        price = item[KEY_PRICE]
        category = dict_catalog[item_id][COLUMN_CATEGORY]
        categories[category] = categories.get(category, 0) + price

    return categories


def print_sales_by_category(sales_by_category: dict):
    items = sorted(sales_by_category, key=sales_by_category.get, reverse=True)[:5]
    for item in items:
        print(" {}: {:.2f} €".format(item, sales_by_category[item]))
    print()

