# Bookbot project

from stats import count_words # importing the count_words function

filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
def main():
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    # print(book_text)

if __name__ == "__main__":
    main()