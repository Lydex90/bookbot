def get_book_text(bookpath):
    with open(bookpath) as f:
        text = f.read()
    return text




def main():
    full_text = get_book_text("books/frankenstein.txt")
    from stats import count_words_in_book
    word_count = count_words_in_book(full_text)

    from stats import count_chars_in_book
    char_count = count_chars_in_book(full_text)
    #print(char_count)
    from stats import sort_char_dictionary

    sorted_char_count = sort_char_dictionary(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()