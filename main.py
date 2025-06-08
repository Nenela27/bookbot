import sys
from stats import get_num_words, get_num_char, dict_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    num_words = get_num_words(book)
    num_char = get_num_char(book)
    dict_sort = dict_sorted(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in dict_sort:
        if char['name'].isalpha():
            print(f"{char['name']}: {char['value']}")

main()