# x = [
#     {
#         "id": 1,
#         "price": 15,
#         "town": "Sofia"
#     },
#     {
#         "id": 2,
#         "price": 15,
#         "town": "pl"
#     },
#     {
#         "id": 3,
#         "price": 15,
#         "town": "Bs"
#     },
#     {
#         "id": 4,
#         "price": 15,
#         "town": "Tx"
#     },
# ]
#
# y = {
#     1: ["ball"],
#     3: ["tshutr"],
#     4: ["ball"]
# }
#
# result = dict()
# for i in filter(lambda product: product["id"] in y, x): result[y[i['id']][0]] = result.get(y[i['id']][0], 0) + i['price']
#
# ff=4

import pandas as pd
CATALOG_FILE = "../resources/catalog.csv"
SALES_FILE = "../resources/sales-10K.csv"

a = pd.read_csv(CATALOG_FILE)
b = pd.read_csv(SALES_FILE)
c = ""