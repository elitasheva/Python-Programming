ASCII_A = 65
ASCII_Z = 90
COUNT_OF_LETTERS = 26
input_key_str = input()
input_message = input()

result_message = ""
try:
    key = int(input_key_str)
    for symbol in input_message:
        num = ord(symbol)
        if ASCII_A <= num <= ASCII_Z:
            num += key
            if num > ASCII_Z:
                num -= COUNT_OF_LETTERS
            result_message += chr(num)
        else:
            result_message += symbol

except ValueError:
    print("INVALID INPUT")

print(result_message)