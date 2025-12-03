def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    total_num_of_words = word_count(book)
    print(f"Found {total_num_of_words} total words")

    
def word_count(book_as_a_string):
    split_string = book_as_a_string.split()
    num_of_words = len(split_string)
    return num_of_words

main()