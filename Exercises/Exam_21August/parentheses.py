
def parChecker(symbolString):
    a = list()
    balanced = True
    index = 0
    count = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(' or symbol == ')':
            if symbol == "(":
                a.append(symbol)
            else:
                if not a:
                    balanced = False
                else:
                    del a[-1]
                    count += 1

        index = index + 1

    if balanced and not a:
        return True, count
    else:
        return False, count


try:
    user_input = input()
    user_input = user_input.strip()

    if not user_input:
        raise ValueError

    result = parChecker(user_input)

    if result[0]:
        print("OK {}".format(result[1]))
    else:
        print("WRONG {}".format(len(user_input)))

except Exception:
    print("INVALID INPUT")

