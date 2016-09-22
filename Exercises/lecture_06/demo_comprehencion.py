from pprint import pprint

CATALOG_FILE = "./resources/catalog.csv"
SALES_FILE = "./resources/sales-10K.csv"

# # list comprehension -> [value_expression for value in iterable]
# with open(CATALOG_FILE) as f:
#     # lines contain all lines from file
#     lines = [l.strip() for l in f]
#     for line in lines:
#         print(line)
#
# numbers = [n for n in range(10) if n % 2 != 0]
# print(numbers)
#
# numbers = [n*2 for n in range(20) if n % 2 == 0]
# print(numbers)


# dict comprehension -> {key_expression: value_expression for value in iterable}
numbers = {n: n*2 for n in range(10)}
for key, value in numbers.items():
    pprint("key: {} -> value: {}". format(key, value))

# with open(CATALOG_FILE) as f:
#     lines = {line_number + 1: l.strip() for line_number, l in enumerate(f)}
#     for key, value in lines.items():
#         pprint("key: {} -> value: {}".format(key, value))

# set comprehension
# numbers = {x % 5 for x in range(10, 50)}
# print(numbers)

# default values
# def print_list(list_to_print):
#     list_to_print = list_to_print or []
#     # for e in list_to_print or []
#     for e in list_to_print:
#         print(e)

# unpacking
# x, y = 100, 200
# print(x)
# print(y)

# x, y, *others = 100, 200, 300, 400
# print(x)
# print(y)
# print(others)

# generators
# def range_equivalen(start, end=None, step=None):
#     step = step if step is not None else 1
#     value = start
#     while end is None or value < end:
#         yield value
#         value += step
#
# debug = ""
# for n in range_equivalen(2, 5):
#     print(n)

# lambda functions
# a_list = [(4, 'b'), (2, 'a'), (1, 'c'), (3, 'f')]
# a_list.sort()
# print(a_list)
#
# a_list.sort(key=lambda item: item[1])
# print(a_list)

# b_list = [n for n in range(10)]
# c_list = list(map((lambda x: x*2), b_list))
# print(c_list)


# def square(r):
#     return r**2
#
#
# def cube(r):
#     return r**3
#
#
# functions = [square, cube]
# for num in range(5):
#     value = map((lambda x: x(num)), functions)
#     print(tuple(value))

# from functools import reduce
#
# filtered_list = list(filter((lambda x: x < 0), range(-5, 5)))
# print(filtered_list)
#
# filtered_list = list(filter((lambda x: x % 2 == 0), range(10)))
# print(filtered_list)
#
# # 1*2 = 2 -> 2*3 = 6 -> 6*4 = 24 multiply the product
# nekfo_value = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# print(nekfo_value)
#
# L = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
# nekuf_string = reduce((lambda x, y: x + y), L)
# print(nekuf_string)

# from lecture_05.catalog import load_catalog
# from itertools import groupby
#
# catalog = load_catalog(CATALOG_FILE)
# catalog = list(catalog.values())
# # catalog.sort(key=lambda item: item[-1])
# sorted_catalog = sorted(catalog, key=lambda item: item[-1])
# grouped_catalog = groupby(sorted_catalog, key=lambda item: item[-1])
# for key, value in grouped_catalog:
#     print("key: {} -> value: {}".format(key, list(value)))



