first_text = input("Enter first text: ")
second_text = input("Enter second text: ")

len_of_second_text = len(second_text)
index = first_text.find(second_text) + len_of_second_text
if index != -1:
     print(first_text[index:])
