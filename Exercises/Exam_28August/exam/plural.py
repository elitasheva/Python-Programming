try:
    user_input = input()

    if not user_input.strip() or not user_input.isalpha():
        raise ValueError

    initial_dict = {
        'y': "ies",
        'o': "es",
        'ch': "es",
        's': "es",
        'sh': "es",
        'x': "es",
        'z': "es"
    }

    plural = None
    for key, value in initial_dict.items():
        if user_input.endswith(key):
            if key == 'y':
                plural = user_input.replace(key, value)
            else:
                plural = user_input + value

            break

    if plural:
        print(plural)
    else:
        plural = user_input + "s"
        print(plural)

except Exception:
    print("INVALID INPUT")