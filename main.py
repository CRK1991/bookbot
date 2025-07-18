# Bookbot project

from stats import count_words # importing the count_words function
from stats import char_count # importing the char_count function
from stats import sort_char_count # importing the sort_char_count function

filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
def main():
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_chars = char_count(book_text)
    sorted_char_count = sort_char_count(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()