from stats import word_count
from stats import char_count
from stats import sorted_list_of_dictionaries

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def sort_on(items):
    return items["num"]

def main():

    path = "books/frankenstein.txt"
    book = get_book_text(path)
    total_num_of_words = word_count(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_num_of_words} total words")
    char_counted = char_count(book)
    sorted_list = sorted_list_of_dictionaries(char_counted)
    sorted_list.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()