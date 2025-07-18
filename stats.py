def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}

    no_caps_text = text.lower()
    for char in no_caps_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_char_count(char_dict):
    char_list = []
    for k, v in char_dict.items():
        if k.isalpha():
            char_list.append({"char": k, "num": v})
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list