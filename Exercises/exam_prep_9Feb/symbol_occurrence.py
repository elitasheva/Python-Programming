# user_input_str = input()
# user_input_str = user_input_str.strip()
#
# if user_input_str:
#     # result = dict((c, user_input_str.count(c)) for c in user_input_str)
#     result = {c: user_input_str.count(c) for c in user_input_str}
#     symbol_with_max_occurrence = max(result, key=result.get)
#     count = result.get(symbol_with_max_occurrence)
#     print(count)
#     print(symbol_with_max_occurrence)
# else:
#     print("INVALID INPUT")
#


import collections
user_input_str = input()
user_input_str = user_input_str.strip()

if user_input_str:
    char_counter = collections.Counter(user_input_str)
    most_common = char_counter.most_common(1)
    print(most_common[0][0])
else:
    print("INVALID INPUT")