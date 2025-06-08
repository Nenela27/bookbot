def get_num_words(book):
    return len(book.split())

def get_num_char(book):
    count_char = {}
    for char in book.lower():
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char

# Sort the dict from greatest to least by the count.
def dict_sorted(dict):
    dict_to_list = []
    for dic in dict:
        dict_to_list.append({'name': dic,'value': dict[dic]})
    return sorted(dict_to_list, reverse=True, key=lambda x: x['value'])