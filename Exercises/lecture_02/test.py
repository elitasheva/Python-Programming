# list
# ------------------------------------------------------------------------------------------
# values = [1, 2, 3, 4, 5, 6, 7, 8]
# print(values[-6:-2:1])
# print(values[-2:-6:-1])
#
# values[2:5] = [55, 66, 77, 88, 99, 111]
# print(values)

# tuple -> wildcard tuple expansion
# a, b, c, *rest = (1, 2, 3, 4, 5, 6, 7)
# print(a)
# print(b)
# print(c)
# print(rest)

# values = (10, 20, 30, 40, 50, 60, 70)
# for index, a in enumerate(values):
#     print("{} -> {}".format(a, index))

# set
# ------------------------------------------------------------------------------------------
# values = {3, 3, 5, 8}
# values2 = set((2,3))
# print(values)

# asd = "We can pass a list to the built-in set function, as we can see in the following"
# my_set = set(asd)
# for char in asd:
#     print(char)

# x = {1, 2, 3}
# y = {3, 4, 5}
# z = set((9, 10))
# for i, a in enumerate(z):
#     print("{}->{}".format(i, a))

# numbers1 = {1, 2, 3, 4, 5}
# numbers2 = set((3, 4, 5, 6, 7))
#
# print(numbers1 & numbers2)
# print(numbers1.intersection(numbers2))
#
# print(numbers1 | numbers2)
# print(numbers1.union(numbers2))
#
# print(numbers1 - numbers2)
# print(numbers1.difference(numbers2))
#
# print(numbers1 ^ numbers2)
# print(numbers1.symmetric_difference(numbers2))

# dict ///OrderedDict(dictionary subclass that remembers the order in which its contents are added)
# ------------------------------------------------------------------------------------------
# weather = {
#     'София': -14,
#     'Новосибирск': -31,
#     'Таити': 30
# }
#
# temp = weather['София']
# print(temp)
#
# weather['София'] = -2
# # print(weather['Бургас']) # keyError
# print(weather.get('Бургас', 'default value'))
#
# for key in weather:
#     print(key)  # при всяка итерация променливата key ще бъде един от ключовете в речника
#     print(weather[key])  # тъй като имаме ключа може да вземем и стойността асоциирана с него
#
# for key, value in weather.items():
#     print(key)
#     print(value)
#
# for value in weather.items():
#     print(value)

# import collections
#
# my_dict = collections.OrderedDict()
# my_dict['a'] = 5
# my_dict['z'] = 5
# my_dict['f'] = 5
# my_dict['c'] = 5
# my_dict['k'] = 5
#
# for key_value_pair in my_dict:
#     print(key_value_pair)
#

temperatures = {
    'София': -14,
    'Новосибирск': -31,
    'Таити': 30,
    'Таити1': [30, 2],
    'Варна': {22, 3},
    'Русе': {
        "temperature": -23,
        "humidity": 90,
    },
    'Пловдив': None,
    'Пазарджик': None
}

print("-" * 20)
print(temperatures)
print(temperatures['София'])
print(temperatures.get('Бургас'))
print(temperatures.get('Бургас', 'No data'))
print(temperatures.get('София', 'No data'))

temp_burgas = temperatures.setdefault('Бургас', -2)
print(temperatures)

print("-" * 20)

key = 'Бургас'
if key in temperatures:
    print(temperatures[key])
else:
    print("No data for {}".format(key))

temperatures['Пловдив'] = 31
print(temperatures)

print("-" * 20)

for city_name in temperatures:
    temperature_data = temperatures[city_name]
    print(city_name, ' -> ', temperature_data)

for neshto in temperatures.items():
    key, value = neshto
    print(neshto)
    print(key)
    print(value)

for city_name, temperature_data in temperatures.items():
    print(city_name, ' -> ', temperature_data)

for temperature_data in temperatures.values():
    print(temperature_data)

print("-" * 20)
print(temperatures.pop('Бургас'))





