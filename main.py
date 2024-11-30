def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_character(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    sorted_value = dict(sorted(num_chars.items(), key=lambda item: item[1], reverse=True))
    for c in sorted_value:
        num = sorted_value[c]
        print(f"The '{c}' character was found {num} times")
    print("--- End report ---")

def get_num_character(text):
    chars_dict = {}
    lowered = text.lower()
    for c in lowered:
        if c.isalpha() == True:
            if c in chars_dict:
                chars_dict[c] += 1
            else:
                chars_dict[c] = 1
    
    return chars_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()