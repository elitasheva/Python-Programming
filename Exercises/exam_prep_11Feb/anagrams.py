path_of_file = input()
key_word = input()


def check_for_anagram(key_list, current_list):
    is_anagram = True

    if len(key_list) != len(current_list):
        is_anagram = False
        return is_anagram

    for i in range(len(key_list)):
        if key_list[i] != current_list[i]:
            is_anagram = False

    return is_anagram


key_word_list = [symbol for symbol in key_word]
key_word_list_sorted = sorted(key_word_list)
result_anagrams = []

with open(path_of_file, encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            current_word_list = [symbol for symbol in line]
            current_word_list_sorted = sorted(current_word_list)
            if check_for_anagram(key_word_list_sorted, current_word_list_sorted):
                result_anagrams.append(line)

result_anagrams_sorted = sorted(result_anagrams)
for word in result_anagrams_sorted:
    if word != key_word:
        print(word)



