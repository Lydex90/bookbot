import sys

def get_book_text(bookpath):
    with open(bookpath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    full_text = get_book_text(sys.argv[1])
    from stats import count_words_in_book
    word_count = count_words_in_book(full_text)

    from stats import count_chars_in_book
    char_count = count_chars_in_book(full_text)
    #print(char_count)
    from stats import sort_char_dictionary

    sorted_char_count = sort_char_dictionary(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()