from lecture_06.refactor_code.sales import load_sales
from lecture_06.refactor_code.catalog import load_catalog
from lecture_06.refactor_code.sales_by_hours import find_sales_by_hours, print_sales_by_hours
from lecture_06.refactor_code.sales_by_town import find_sales_by_town, print_sales_by_town
from lecture_06.refactor_code.sales_by_category import find_sales_by_category, print_sales_by_category
from lecture_06.refactor_code.sales_summary import print_summary

CATALOG_FILE = "../resources/catalog.csv"
SALES_FILE = "../resources/sales-10K.csv"


dict_catalog = load_catalog(CATALOG_FILE)
list_sales = load_sales(SALES_FILE)

print("""Обобщение
---------""")
print_summary(list_sales)

print("""Сума на продажби по категории (top 5)
-----------------------------""")
sales_by_category = find_sales_by_category(dict_catalog, list_sales)
print_sales_by_category(sales_by_category)


print("""Сума на продажби по градове (top 5)
-----------------------------""")
sales_by_town = find_sales_by_town(list_sales)
# print_sales_by_town(sales_by_town)


print("""Сума на продажби по час (top 5)
-----------------------------""")
sales_by_hours = find_sales_by_hours(list_sales)
print_sales_by_hours(sales_by_hours)



