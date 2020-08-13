# Date: Wed, 8/12/20
# Question: Hashtable Word Count

import re


def hashtable_word_count(S: str):
    word_count_map = {}
    trimmed_string = re.sub("[^a-zA-Z ]+", "", S)
    string_array = trimmed_string.split()
    string_array = [s.lower() for s in string_array]
    for string in string_array:
        if word_count_map.get(string):
            word_count_map[string] = word_count_map.get(string)+1
        else:
            word_count_map[string] = 1
    return word_count_map


if __name__ == '__main__':

    print(hashtable_word_count("Monkey sees monkey do"))
    print("Expect: monkey: 2, sees: 1, do: 1")

    print(hashtable_word_count("i, I, I - Love Lucy, I really do!"))
    print("Expect: Lucy: 1, I: 4, Love: 1, really: 1, do: 1")

    print(hashtable_word_count("i, I,         I - Love Lucy,     I really do!"))
    print("Expect: Lucy: 1, I: 4, Love: 1, really: 1, do: 1")
