
def count_words_in_book(book):
    book_list = book.split()
    return len(book_list)

def count_chars_in_book(book):
    char_list = {}

    for char in book:
        if char.lower() in char_list:
            char_list[char.lower()] += 1
        else:
            char_list[char.lower()] = 1

    return char_list

def sort_on(dict):
    return dict["num"]

def sort_char_dictionary(dict):
    sorted_list = []
    for char, count in dict.items():
        sorted_list.append({"char":char, "num":count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

