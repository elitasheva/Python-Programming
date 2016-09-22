user_input = input()

numbers_as_str = user_input.split()
index = None

try:
    prev_num = None
    for idx, num_str in enumerate(numbers_as_str):
        num = int(num_str)

        if prev_num is None or num >= prev_num:
            prev_num = num
            continue
        else:
            index = idx
            break

    if index:
        print(index)
    else:
        print("SORTED")

except Exception:
    print("INVALID INPUT")

