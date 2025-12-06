def word_count(book_as_a_string):
    split_string = book_as_a_string.split()
    num_of_words = len(split_string)
    return num_of_words

def char_count(book_as_a_string):
    string = book_as_a_string.lower()
    char_dict = {}
    for letter in string:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1            
    return char_dict

def sorted_list_of_dictionaries(letters_dict):
    sorted_list = []
    for entry in letters_dict:
        sorted_list.append({"char": entry, "num": letters_dict[entry]})
    return sorted_list
